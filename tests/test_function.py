"""test_function

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from datetime import datetime

from flask import url_for
from eve import Eve
import pytest


@pytest.mark.function
def test_function_field(client: Eve, sample_schema: dict):
    """Test to ensure field option works in function

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][1]["function"] = "field['foo']"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert all([row['foo'] == row['bar'] for row in res.json])


@pytest.mark.function
def test_function_this(client: Eve, sample_schema: dict):
    """Test to ensure this option works in function

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["args"]["elements"] = [1]
    sample_schema["columns"][0]["function"] = "this * 3"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert all([row['foo'] > 2 for row in res.json])


@pytest.mark.function
def test_function_conditionals(client: Eve, sample_schema: dict):
    """Test to ensure built-in 'None' works in function

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 10
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["percent_empty"] = 0.5
    sample_schema["columns"][1]["function"] = "'FULL' if field[\"foo\"] != None else \"EMPTY\""

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert len(res.json) == 10
    assert all([row['bar'] == 'FULL' if row['foo'] else row['bar'] == 'EMPTY' for row in res.json])


@pytest.mark.function
def test_function_restrict(client: Eve, sample_schema: dict):
    """Test to ensure function restricts use

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = "__import__('platform').system()"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 400
    assert res.mimetype == 'application/json'


@pytest.mark.function
def test_function_abs(client: Eve, sample_schema: dict):
    """Test to ensure abs function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["type"] = "random_int"
    sample_schema["columns"][0]["args"] = {"min": -10, "max": -1}
    sample_schema["columns"][0]["function"] = "abs(this)"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] > 0


@pytest.mark.function
def test_function_age_rounding(client: Eve, sample_schema: dict):
    """Test to ensure only whole years are counted for age function

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["type"] = "date_between"
    sample_schema["columns"][0]["args"] = {"start_date": "-364d", "end_date": "-363d"}
    sample_schema["columns"][0]["function"] = "age(parse_date(this, '%Y-%m-%d'))"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == 0


@pytest.mark.function
def test_function_age_invalid(client: Eve, sample_schema: dict):
    """Test to ensure non-dates raise TypeError

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: TypeError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = "age(this)"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 400


@pytest.mark.function
def test_function_bool(client: Eve, sample_schema: dict):
    """Test to ensure bool function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["args"] = {"elements": [0]}
    sample_schema["columns"][0]["function"] = "bool(this)"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] is False


@pytest.mark.function
def test_function_concat(client: Eve, sample_schema: dict):
    """Test to ensure concat function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["args"] = {"elements": ["hello"]}
    sample_schema["columns"][1]["args"] = {"elements": ["world"]}
    sample_schema["columns"].append({
        "name": "baz",
        "type": "pybool",
        "function": "concat(field['foo'], field['bar'])"
    })

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['baz'] == "helloworld"


@pytest.mark.function
def test_function_day(client: Eve, sample_schema: dict):
    """Test to ensure day function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = "day(now())"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == datetime.now().day


@pytest.mark.function
def test_function_format_date(client: Eve, sample_schema: dict):
    """Test to ensure date formatting function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = "format_date(now(), '%Y-%m-%d')"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == datetime.now().strftime('%Y-%m-%d')


@pytest.mark.function
def test_function_float(client: Eve, sample_schema: dict):
    """Test to ensure float function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["type"] = "random_int"
    sample_schema["columns"][0]["args"] = {}
    sample_schema["columns"][0]["function"] = "float(this)"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert isinstance(res.json[0]['foo'], float)


@pytest.mark.function
def test_function_hash(client: Eve, sample_schema: dict):
    """Test to ensure hash function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = "hash(this)"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert isinstance(res.json[0]['foo'], int)


@pytest.mark.function
def test_function_int(client: Eve, sample_schema: dict):
    """Test to ensure int function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["args"] = {"elements": ["1"]}
    sample_schema["columns"][0]["function"] = "int(this)"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert isinstance(res.json[0]['foo'], int)


@pytest.mark.function
def test_function_isinstance(client: Eve, sample_schema: dict):
    """Test to ensure isinstance function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["args"] = {"elements": [1.999999]}
    sample_schema["columns"][0]["function"] = "isinstance(this, float)"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] is True


@pytest.mark.function
def test_function_join(client: Eve, sample_schema: dict):
    """Test to ensure join function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["type"] = "random_choices"
    sample_schema["columns"][0]["args"] = {"length": 2}
    sample_schema["columns"][0]["function"] = "join(this, ',')"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert len(res.json[0]['foo'].split(',')) == 2


@pytest.mark.function
def test_function_len(client: Eve, sample_schema: dict):
    """Test to ensure len function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][1]["function"] = "len(field['foo'])"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['bar'] == len(res.json[0]['foo'])


@pytest.mark.function
def test_function_lower(client: Eve, sample_schema: dict):
    """Test to ensure lower function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["args"] = {"elements": ["FOO"]}
    sample_schema["columns"][0]["function"] = "lower(this)"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == "foo"


@pytest.mark.function
def test_function_month(client: Eve, sample_schema: dict):
    """Test to ensure month function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = "month(now())"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == datetime.now().month


@pytest.mark.function
def test_function_parse_date(client: Eve, sample_schema: dict):
    """Test to ensure parse_date function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["type"] = "date"
    del sample_schema["columns"][0]["args"]
    sample_schema["columns"][0]["function"] = "isinstance(parse_date(this, '%Y-%m-%d'), datetime)"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo']


@pytest.mark.function
def test_function_pow(client: Eve, sample_schema: dict):
    """Test to ensure pow function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["args"] = {"elements": [2]}
    sample_schema["columns"][1]["args"] = {"elements": [3]}
    sample_schema["columns"].append({
        "name": "baz",
        "type": "random_element",
        "function": "pow(field['foo'], field['bar'])"
    })

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['baz'] == 8


@pytest.mark.function
def test_function_round(client: Eve, sample_schema: dict):
    """Test to ensure round function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["args"] = {"elements": [1.999999]}
    sample_schema["columns"][0]["function"] = "round(this, 2)"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == 2.0


@pytest.mark.function
def test_function_split(client: Eve, sample_schema: dict):
    """Test to ensure split function works

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["args"] = {"elements": ["hello,world"]}
    sample_schema["columns"][0]["function"] = "split(this, ',')"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == ["hello", "world"]


@pytest.mark.function
def test_function_str(client: Eve, sample_schema: dict):
    """Test to ensure str function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["type"] = "random_int"
    sample_schema["columns"][0]["args"] = {}
    sample_schema["columns"][0]["function"] = "str(this)"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert isinstance(res.json[0]['foo'], str)


@pytest.mark.function
def test_function_sum(client: Eve, sample_schema: dict):
    """Test to ensure sum function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["type"] = "random_element"
    sample_schema["columns"][0]["args"] = {"elements": [1]}
    sample_schema["columns"][1]["type"] = "random_element"
    sample_schema["columns"][1]["args"] = {"elements": [2]}

    sample_schema["columns"].append({
        "name": "baz",
        "type": "random_int",
        "function": "sum((field['foo'], field['bar']))"
    })

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['baz'] == 3


@pytest.mark.function
def test_function_upper(client: Eve, sample_schema: dict):
    """Test to ensure upper function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = "upper(this)"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == "THIS"


@pytest.mark.function
def test_function_year(client: Eve, sample_schema: dict):
    """Test to ensure year function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = "year(now())"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == datetime.now().year


@pytest.mark.function
def test_function_epoch(client: Eve, sample_schema: dict):
    """Test to ensure epoch function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = "epoch(now())"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert isinstance(res.json[0]['foo'], float)


@pytest.mark.function
def test_function_time(client: Eve, sample_schema: dict):
    """Test to ensure time function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = "str(time(now()))"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'].split('.')[0] == str(datetime.now().time()).split('.')[0]


@pytest.mark.function
def test_function_request_param(client: Eve, sample_schema: dict):
    """Test to ensure request parameter function works

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = "request_param('extra_param')"

    res = client.post(url_for('custom_schema', extra_param="this is happening?"), json=sample_schema,
                      headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == "this is happening?"


@pytest.mark.function
def test_function_additional_args(client: Eve, sample_schema: dict):
    """Test to ensure additional

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["args"] = {"elements": ["this"], "foo": "bar"}

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 400


@pytest.mark.function
def test_invalid_function(client: Eve, sample_schema: dict):
    """Test to ensure field option works in function

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][1]["function"] = "if else"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 400
    assert res.mimetype == 'application/json'
