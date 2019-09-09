"""test_function

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from datetime import datetime

from flask import url_for
import pytest


@pytest.mark.function
def test_function_field(client, sample_schema):
    """Test to ensure field option works in function

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][1]["function"] = "field['foo']"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert all([row['foo'] == row['bar'] for row in res.json])


@pytest.mark.function
def test_function_this(client, sample_schema):
    """Test to ensure this option works in function

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["args"]["elements"] = [1]
    sample_schema["columns"][0]["function"] = "this * 3"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert all([row['foo'] > 2 for row in res.json])


@pytest.mark.function
def test_function_conditionals(client):
    """Test to ensure built-in 'None' works in function

    :param Flask client: Mockerena app instance
    :return:
    """

    data = {
        "schema": "test_schema",
        "num_rows": 10,
        "file_format": "json",
        "file_name": "test_{}_schema",
        "columns": [
            {
                "name": "foo",
                "type": "word",
                "percent_empty": 0.5
            },
            {
                "name": "bar",
                "type": "word",
                "function": "'FULL' if field[\"foo\"] != None else \"EMPTY\""
            }
        ]
    }

    res = client.post(url_for('custom_schema'), json=data, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert len(res.json) == 10
    assert all([row['bar'] == 'FULL' if row['foo'] else row['bar'] == 'EMPTY' for row in res.json])


@pytest.mark.function
def test_function_restrict(client, sample_schema):
    """Test to ensure function restricts use

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = "__import__('platform').system()"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert all([row['foo'] == 'this' for row in res.json])


@pytest.mark.function
def test_function_abs(client):
    """Test to ensure abs function works

    :param Flask client: Mockerena app instance
    :return:
    """

    data = {
        "schema": "test_schema",
        "num_rows": 1,
        "file_format": "json",
        "file_name": "test_{}_schema",
        "columns": [
            {
                "name": "foo",
                "type": "random_int",
                "args": {
                    "min": -10,
                    "max": -1
                },
                "function": "abs(this)"
            }
        ]
    }

    res = client.post(url_for('custom_schema'), json=data, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] > 0


@pytest.mark.function
def test_function_bool(client):
    """Test to ensure bool function works

    :param Flask client: Mockerena app instance
    :return:
    """

    data = {
        "schema": "test_schema",
        "num_rows": 1,
        "file_format": "json",
        "file_name": "test_{}_schema",
        "columns": [
            {
                "name": "foo",
                "type": "random_element",
                "args": {
                    "elements": [0],
                },
                "function": "bool(this)"
            }
        ]
    }

    res = client.post(url_for('custom_schema'), json=data, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] is False


@pytest.mark.function
def test_function_concat(client):
    """Test to ensure concat function works

    :param Flask client: Mockerena app instance
    :return:
    """

    data = {
        "schema": "test_schema",
        "num_rows": 1,
        "file_format": "json",
        "file_name": "test_{}_schema",
        "columns": [
            {
                "name": "foo",
                "type": "random_element",
                "args": {
                    "elements": ["hello"],
                }
            },
            {
                "name": "bar",
                "type": "random_element",
                "args": {
                    "elements": ["world"],
                }
            },
            {
                "name": "baz",
                "type": "random_int",
                "function": "concat(field['foo'], field['bar'])"
            }
        ]
    }

    res = client.post(url_for('custom_schema'), json=data, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['baz'] == "helloworld"


@pytest.mark.function
def test_function_day(client):
    """Test to ensure day function works

    :param Flask client: Mockerena app instance
    :return:
    """

    data = {
        "schema": "test_schema",
        "num_rows": 1,
        "file_format": "json",
        "file_name": "test_{}_schema",
        "columns": [
            {
                "name": "foo",
                "type": "random_element",
                "function": "day(now())"
            }
        ]
    }

    res = client.post(url_for('custom_schema'), json=data, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == datetime.now().day


@pytest.mark.function
def test_function_float(client):
    """Test to ensure float function works

    :param Flask client: Mockerena app instance
    :return:
    """

    data = {
        "schema": "test_schema",
        "num_rows": 1,
        "file_format": "json",
        "file_name": "test_{}_schema",
        "columns": [
            {
                "name": "foo",
                "type": "random_int",
                "function": "float(this)"
            }
        ]
    }

    res = client.post(url_for('custom_schema'), json=data, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert isinstance(res.json[0]['foo'], float)


@pytest.mark.function
def test_function_hash(client):
    """Test to ensure hash function works

    :param Flask client: Mockerena app instance
    :return:
    """

    data = {
        "schema": "test_schema",
        "num_rows": 1,
        "file_format": "json",
        "file_name": "test_{}_schema",
        "columns": [
            {
                "name": "foo",
                "type": "random_element",
                "args": {
                    "elements": ["foo"],
                },
                "function": "hash(this)"
            }
        ]
    }

    res = client.post(url_for('custom_schema'), json=data, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert isinstance(res.json[0]['foo'], int)


@pytest.mark.function
def test_function_int(client):
    """Test to ensure int function works

    :param Flask client: Mockerena app instance
    :return:
    """

    data = {
        "schema": "test_schema",
        "num_rows": 1,
        "file_format": "json",
        "file_name": "test_{}_schema",
        "columns": [
            {
                "name": "foo",
                "type": "random_element",
                "args": {
                    "elements": ["1"],
                },
                "function": "int(this)"
            }
        ]
    }

    res = client.post(url_for('custom_schema'), json=data, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert isinstance(res.json[0]['foo'], int)


@pytest.mark.function
def test_function_isinstance(client):
    """Test to ensure isinstance function works

    :param Flask client: Mockerena app instance
    :return:
    """

    data = {
        "schema": "test_schema",
        "num_rows": 1,
        "file_format": "json",
        "file_name": "test_{}_schema",
        "columns": [
            {
                "name": "foo",
                "type": "random_element",
                "args": {
                    "elements": [1.999999],
                },
                "function": "isinstance(this, float)"
            }
        ]
    }

    res = client.post(url_for('custom_schema'), json=data, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] is True


@pytest.mark.function
def test_function_join(client):
    """Test to ensure join function works

    :param Flask client: Mockerena app instance
    :return:
    """

    data = {
        "schema": "test_schema",
        "num_rows": 1,
        "file_format": "json",
        "file_name": "test_{}_schema",
        "columns": [
            {
                "name": "foo",
                "type": "random_choices",
                "args": {
                    "length": 2
                },
                "function": "join(this, ',')"
            }
        ]
    }

    res = client.post(url_for('custom_schema'), json=data, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert len(res.json[0]['foo'].split(',')) == 2


@pytest.mark.function
def test_function_len(client, sample_schema):
    """Test to ensure len function works

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][1]["function"] = "len(field['foo'])"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['bar'] == len(res.json[0]['foo'])


@pytest.mark.function
def test_function_lower(client):
    """Test to ensure lower function works

    :param Flask client: Mockerena app instance
    :return:
    """

    data = {
        "schema": "test_schema",
        "num_rows": 1,
        "file_format": "json",
        "file_name": "test_{}_schema",
        "columns": [
            {
                "name": "foo",
                "type": "random_element",
                "args": {
                    "elements": ["FOO"],
                },
                "function": "lower(this)"
            }
        ]
    }

    res = client.post(url_for('custom_schema'), json=data, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == "foo"


@pytest.mark.function
def test_function_month(client, sample_schema):
    """Test to ensure month function works

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = "month(now())"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == datetime.now().month


@pytest.mark.function
def test_function_pow(client):
    """Test to ensure pow function works

    :param Flask client: Mockerena app instance
    :return:
    """

    data = {
        "schema": "test_schema",
        "num_rows": 1,
        "file_format": "json",
        "file_name": "test_{}_schema",
        "columns": [
            {
                "name": "foo",
                "type": "random_element",
                "args": {
                    "elements": [2],
                }
            },
            {
                "name": "bar",
                "type": "random_element",
                "args": {
                    "elements": [3],
                }
            },
            {
                "name": "baz",
                "type": "random_element",
                "function": "pow(field['foo'], field['bar'])"
            }
        ]
    }

    res = client.post(url_for('custom_schema'), json=data, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['baz'] == 8


@pytest.mark.function
def test_function_round(client):
    """Test to ensure round function works

    :param Flask client: Mockerena app instance
    :return:
    """

    data = {
        "schema": "test_schema",
        "num_rows": 1,
        "file_format": "json",
        "file_name": "test_{}_schema",
        "columns": [
            {
                "name": "foo",
                "type": "random_element",
                "args": {
                    "elements": [1.999999],
                },
                "function": "round(this, 2)"
            }
        ]
    }

    res = client.post(url_for('custom_schema'), json=data, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == 2.0


@pytest.mark.function
def test_function_split(client):
    """Test to ensure split function works

    :param Flask client: Mockerena app instance
    :return:
    """

    data = {
        "schema": "test_schema",
        "num_rows": 1,
        "file_format": "json",
        "file_name": "test_{}_schema",
        "columns": [
            {
                "name": "foo",
                "type": "random_element",
                "args": {
                    "elements": ["hello,world"]
                },
                "function": "split(this, ',')"
            }
        ]
    }

    res = client.post(url_for('custom_schema'), json=data, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == ["hello", "world"]


@pytest.mark.function
def test_function_str(client, sample_schema):
    """Test to ensure str function works

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
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
def test_function_sum(client, sample_schema):
    """Test to ensure sum function works

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
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
def test_function_upper(client, sample_schema):
    """Test to ensure upper function works

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = "upper(this)"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == "THIS"


@pytest.mark.function
def test_function_year(client, sample_schema):
    """Test to ensure year function works

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = "year(now())"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == datetime.now().year


@pytest.mark.function
def test_function_epoch(client, sample_schema):
    """Test to ensure epoch function works

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = "epoch(now())"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert isinstance(res.json[0]['foo'], float)


@pytest.mark.function
def test_function_time(client, sample_schema):
    """Test to ensure time function works

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = "str(time(now()))"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'].split('.')[0] == str(datetime.now().time()).split('.')[0]


@pytest.mark.function
def test_function_request_param(client, sample_schema):
    """Test to ensure request parameter function works

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = "request_param('extra_param')"

    res = client.post(url_for('custom_schema', extra_param="this is happening?"), json=sample_schema,
                      headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == "this is happening?"
