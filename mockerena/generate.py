"""Helper methods for generating data

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

import datetime
import random
import re

from faker import Faker
from flask import request
from mockerena.providers import MockProvider
from mockerena.settings import DEFAULT_SIZE

fake = Faker()
fake.add_provider(MockProvider)


def age(date: datetime.datetime) -> int:
    """Returns age in years for a given date

    :param datetime.datetime date: Datetime or date
    :return:
    """

    now = datetime.date.today()

    if isinstance(date, (datetime.date, datetime.datetime)):
        return now.year - date.year - 1 \
            if now.month < date.month or (now.month == date.month and now.day < date.day) else now.year - date.year

    return date


APPROVED_GLOBALS = {
    'abs': abs,
    'age': age,
    'bool': bool,
    'concat': lambda *args: "".join(args),
    'day': lambda d: d.day if isinstance(d, (datetime.datetime, datetime.date)) else d,
    'epoch': lambda d: d.timestamp() if isinstance(d, (datetime.datetime, datetime.date)) else d,
    'fake': fake,
    'float': float,
    'format_date': datetime.datetime.strftime,
    'hash': hash,
    'int': int,
    'isinstance': isinstance,
    'join': lambda l, d: d.join(l) if isinstance(d, str) and isinstance(l, (list, tuple)) else '',
    'len': len,
    'lower': lambda s: str(s).lower(),
    'month': lambda d: d.month if isinstance(d, (datetime.datetime, datetime.date)) else d,
    'now': datetime.datetime.now,
    'pow': pow,
    'request_param': lambda param: request.args.get(param, None),
    'range': range,
    'round': round,
    'split': lambda s, d: s.split(d) if isinstance(s, str) else s,
    'str': str,
    'sum': sum,
    'time': lambda d: d.time() if isinstance(d, datetime.datetime) else d,
    'upper': lambda s: str(s).upper(),
    'year': lambda d: d.year if isinstance(d, (datetime.datetime, datetime.date)) else d
}

APPROVED_TERMS = [
    "[\\+\\-\\*{1,2}\\/{1,2}%]",  # Operators
    "(?:and|f?or|!=|={2}|i[sn]|not|>=?|<=?|)",  # Logic
    "(?:if|else)",  # Conditionals
    "(?:True|False|None|-?\\d+|\"{2}|\'{2}|\'[\\w\\\\/,: ]+\'|\"[\\w\\\\/,: ]+\")",  # Built-ins
    f"(?:{'|'.join(APPROVED_GLOBALS)})\\.?\\([\\w\\'\\\"\\[\\]\\(\\)\\\\+\\%*,-: ]+\\)",  # Functions
    "(?:fake|request_param)\\.[\\w]+\\([\\w\\'\\\"\\[\\]\\(\\)\\{\\}\\+*,-: ]+\\)",  # Faker
    "(?:this|field\\[[\'\"][\\w\\. ]+[\'\"]\\])",  # Variables
    "\\[-?\\d+(?: ?\\: ?-?\\d+)?\\]",  # Slicing
    " "  # Whitespace
]

PATTERN = re.compile(f"^(?:{'|'.join(APPROVED_TERMS)})+$")


def is_safe(expression: str) -> bool:
    """Returns true if the expression is safe to execute

    :param str expression: Python expression
    :return:
    """

    return bool(re.match(PATTERN, expression))


def data_for_column(column: dict, kwargs: dict, size: int) -> list:
    """Generates data for schema column

    :param dict column: Column definition
    :param dict kwargs: Faker keyword arguments
    :param int size: Number of rows
    :return:
    """

    data = []
    data_type = column.get('type', 'empty')
    method = getattr(fake, data_type)
    percent_empty = column.get('percent_empty', 0)

    for _ in range(size):

        if random.random() <= percent_empty:
            data.append(None)

        else:
            datum = method(**kwargs)
            if 'format' in column:
                datum = datum.strftime(column['format']) if isinstance(datum, (datetime.date, datetime.datetime)) \
                    else datum
            data.append(datum)

    return data


def generate_data(schema: dict) -> dict:
    """Generates sample data from a schema

    :param dict schema: Provider integration data schema
    :return:
    """

    size = int(request.args.get('numrows', schema.get('num_rows', DEFAULT_SIZE)))
    mock = {column['name']: data_for_column(column, column.get('args', {}), size) for column in schema['columns']}
    functions = {col['name']: col['function'] for col in filter(lambda col: 'function' in col, schema['columns'])
                 if is_safe(col['function'])}

    if functions:

        approved_locals = {'param': request.args}  # 'param' can be used to evaluate

        for row in range(0, size):
            approved_locals['field'] = {column: mock[column][row] for column in mock}
            for column in functions:
                approved_locals['this'] = approved_locals['field'][column]  # 'this' can be referenced in function
                mock[column][row] = eval(functions[column], APPROVED_GLOBALS, approved_locals)  # pylint: disable=W0123

    return mock
