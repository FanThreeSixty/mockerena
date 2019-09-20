"""Helper methods for formatting the output of data

.. codeauthor:: Michael Holtzscher <mholtzscher@fanthreesixty.com>
.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

import datetime
from functools import reduce
import json
import random
from typing import Any

from flask import make_response, request
from jinja2 import Template
import pandas as pd

from mockerena.errors import ERROR_422
from mockerena.generate import fake
from mockerena.settings import DEFAULT_FILE_FORMAT, DEFAULT_INCLUDE_HEAD, DEFAULT_SIZE, DEFAULT_QUOTE_CHARACTER,\
    DEFAULT_EXCLUDE_NULL, DEFAULT_DELIMITER, DEFAULT_KEY_SEPARATOR, DEFAULT_IS_NESTED, DEFAULT_RESPONSES


def to_boolean(var: Any) -> bool:
    """Convert string or object to boolean

    :param var: String or object
    :return:
    """

    return var.lower() in ("true", "yes", "y", "1") if isinstance(var, str) else bool(var)


def un_flatten(data: dict, separator: str = '.'):
    """Un-flatten a dictionary

    :param dict data: Dictionary data
    :param str separator: Key separator
    :return:
    """

    def _un_flatten(acc: dict, item: tuple) -> dict:
        """Recursively un-flatten dictionary

        :param dict acc: Dictionary data output
        :param tuple item: Key, value pairs
        :return:
        """

        key, *terms = str(item[0]).split(separator, 1)
        _ = _un_flatten(acc.setdefault(key, {}), (terms[0], item[1])) if terms else acc.update({key: item[1]})
        return acc

    return reduce(_un_flatten, data.items(), {})


def format_output(mock: dict, schema: dict):  # pylint: disable=R0914
    """Formats output as defined in schema

    :param dict mock: Mock data
    :param dict schema: Provider integration data schema
    :return:
    """

    file_format = request.args.get('file_format', schema.get('file_format', DEFAULT_FILE_FORMAT))
    include_header = to_boolean(request.args.get('include_header', schema.get('include_header', DEFAULT_INCLUDE_HEAD)))
    exclude_null = to_boolean(request.args.get('exclude_null', schema.get('exclude_null', DEFAULT_EXCLUDE_NULL)))
    size = int(request.args.get('numrows', schema.get('num_rows', DEFAULT_SIZE)))
    delimiter = schema.get('delimiter', DEFAULT_DELIMITER)
    quote_character = schema.get('quote_character', DEFAULT_QUOTE_CHARACTER)
    key_separator = schema.get('key_separator', DEFAULT_KEY_SEPARATOR)
    is_nested = schema.get('is_nested', DEFAULT_IS_NESTED)
    truncated_columns = [column['name'] for column in filter(lambda c: c.get('truncate', False), schema.get('columns'))]

    # Determine how the service will respond
    responses = schema.get('responses', DEFAULT_RESPONSES)
    responses = responses if isinstance(responses, (list, tuple)) and responses else DEFAULT_RESPONSES
    response = random.choices(responses, weights=[response.get('weight', 1) for response in responses])[0]
    status_code = response.get('status_code', 200)
    headers = response.get('headers', None)

    # Remove truncated columns
    for column in truncated_columns:
        mock.pop(column, None)

    if isinstance(response.get('data'), str):
        content = response.get('data')
        content_type = response.get('content_type', 'text/plain')

    elif file_format in ('csv', 'tsv'):
        _delimiter = delimiter or ('\t' if file_format == 'tsv' else ',')
        content = _format_pandas(mock, _delimiter, include_header, quote_character)
        content_type = response.get('content_type', 'text/csv')

    elif file_format == 'json':
        content = _format_json(mock, sep=key_separator, exclude_null=exclude_null, is_nested=is_nested)
        content_type = response.get('content_type', 'application/json')

    elif file_format == 'sql':

        def get_row(row):
            return tuple([mock[column][row] for column in mock.keys()])

        table_name = schema.get('table_name', 'EXAMPLE_DATA')
        fields = ', '.join(mock.keys())
        content = "\n".join([f"INSERT INTO {table_name} ({fields}) VALUES {get_row(row)};" for row in range(0, size)])
        content_type = response.get('content_type', 'application/sql')

    elif schema.get('template', None):

        key_words = {
            "include_header": include_header,
            "request_param": request.args,
            "fake": fake,
            "exclude_null": exclude_null
        }

        content = _format_template(mock, schema, **key_words)
        content_type = response.get('content_type', f'text/{file_format}')

    else:

        error = {
            "_status": "ERR",
            "_issues": {
                "validation exception": f"You must provide a template for file format '{str(file_format)}'."
            },
            "_error": ERROR_422
        }

        return json.dumps(error), 422, {'Content-Type': 'application/json'}

    now = datetime.datetime.now().strftime("%Y%m%d%H%M")
    filename = schema.get('file_name').format(now)

    resp = make_response(content, status_code)
    resp.headers["Content-Type"] = content_type
    resp.headers["Content-Disposition"] = f'attachment; filename={filename}.{file_format}'

    if headers:
        for header in headers:
            resp.headers[header] = headers[header]

    return resp


def _format_pandas(mock: dict, sep: str, header: bool, quote_character: str = '"') -> str:
    """Returns mock data as csv format

    :param dict mock: Mock data
    :param str sep: Column delimiter
    :param bool header: File headers if any
    :param str quote_character: Character used to quote fields
    :return:
    """

    return pd.DataFrame(mock).to_csv(sep=sep, index=None, header=header, quotechar=quote_character)


def _format_json(mock: dict, sep: str, exclude_null: bool = False, is_nested: bool = True) -> str:
    """Returns mock data in json format

    :param dict mock: Mock data
    :param str sep: Nested attribute key separator
    :param bool exclude_null: Exclude null entries
    :param bool is_nested: Un-flatten json by separating keys
    :return:
    """

    data_frame = pd.DataFrame(mock)
    records = [row.dropna().to_dict() if exclude_null else row.to_dict() for _, row in data_frame.iterrows()]
    return json.dumps([un_flatten(record, sep) if is_nested else record for record in records])


def _format_template(mock: dict, schema: dict, **kwargs) -> str:
    """Returns mock data in html format

    :param dict mock: Mock data
    :param dict schema: Provider integration data schema
    :return:
    """

    data = pd.DataFrame(mock).to_dict(orient='records')
    return Template(schema['template']).render(records=data, **kwargs)
