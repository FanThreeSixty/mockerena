"""test_schemas

.. codeauthor:: Michael Holtzscher <mholtzscher@fanthreesixty.com>
.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from datetime import datetime
import pytest
from eve import Eve
from flask import url_for


@pytest.mark.schema
def test_get_all_schemas(client: Eve):
    """Tests that results are returned for get_all_schemas

    :param Eve client: Mockerena app instance
    :raises: AssertionError
    """

    res = client.get(url_for('schema|resource'))
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json


@pytest.mark.schema
def test_generate_by_schema_id(client: Eve):
    """Test to ensure a user can generate data for a schema by id

    :param Eve client: Mockerena app instance
    :raises: AssertionError
    """

    res = client.get(url_for('schema|item_lookup', _id='mock_example'))
    assert res.status_code == 200

    data = res.json

    res = client.get(url_for('generate', schema_id=data['_id']))
    assert res.status_code == 200
    assert res.mimetype == 'text/csv'


@pytest.mark.schema
def test_missing_generate_schema(client: Eve):
    """Test to ensure a missing schema returns a 500

    :param Eve client: Mockerena app instance
    :raises: AssertionError
    """

    message = "The requested URL was not found on the server.  If you entered the URL manually please " \
              "check your spelling and try again."

    res = client.get(url_for('generate', schema_id='foo_bar'))
    assert res.status_code == 404
    assert res.json["_status"] == "ERR"
    assert res.json["_error"]["code"] == 404
    assert res.json["_error"]["message"] == message


@pytest.mark.schema
def test_missing_schema(client: Eve):
    """Test to ensure a missing schema returns a 500

    :param Eve client: Mockerena app instance
    :raises: AssertionError
    """

    message = "The requested URL was not found on the server. If you entered the URL manually please " \
              "check your spelling and try again."

    res = client.get(url_for('schema|item_lookup', _id='foo_bar'))
    assert res.status_code == 404
    assert res.json["_status"] == "ERR"
    assert res.json["_error"]["code"] == 404
    assert res.json["_error"]["message"] == message


@pytest.mark.malformed
@pytest.mark.schema
def test_malformed_schema(client: Eve):
    """Test to ensure the proper error returns for malformed input

    :param Eve client: Mockerena app instance
    :raises: AssertionError
    """

    data = [
        "What is this?"
    ]

    message = "Data generation failure: 1 document(s) contain(s) error(s)"

    res = client.post(url_for('custom_schema'), json=data, headers={'Content-Type': "application/json"})
    assert res.status_code == 422
    assert res.json["_status"] == "ERR"
    assert res.json["_error"]["code"] == 422
    assert res.json["_error"]["message"] == message


@pytest.mark.delimiter
@pytest.mark.schema
def test_function_delimiter(client: Eve, sample_schema: dict):
    """Test to ensure delimiter is working

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["delimiter"] = "|"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'text/csv'
    assert str(res.get_data()).count('|') == sample_schema["num_rows"] + 1


@pytest.mark.delimiter
@pytest.mark.schema
def test_function_invalid_delimiter(client: Eve, sample_schema: dict):
    """Test to ensure invalid delimiters are defaulted to comma or tab

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["delimiter"] = "   "

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'text/csv'
    assert str(res.get_data()).count(',') == sample_schema["num_rows"] + 1


@pytest.mark.template
@pytest.mark.schema
def test_function_template(client: Eve, sample_schema: dict):
    """Test to ensure template is working

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "html"
    sample_schema["template"] = "{% for r in records %}<span>{{r['foo']}}</span><span>{{r['bar']}}</span>{% endfor %}"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'text/html'
    assert res.get_data().decode('utf-8') == "<span>this</span><span>that</span>"


@pytest.mark.template
@pytest.mark.schema
def test_missing_template(client: Eve, sample_schema: dict):
    """Test to ensure template is working

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "html"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})

    assert res.status_code == 422
    assert res.json["_status"] == "ERR"
    assert res.json["_issues"]["validation exception"] == "You must provide a template for file format 'html'."
    assert res.json["_error"]["code"] == 422
    assert res.json["_error"]["message"] == "Data generation failure: 1 document(s) contain(s) error(s)"


@pytest.mark.nested
@pytest.mark.schema
@pytest.mark.parametrize('is_nested', (True, False))
def test_nested_json(client: Eve, sample_schema: dict, is_nested: bool):
    """Test to ensure is_nested is working

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :param bool is_nested: JSON is nested
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["name"] = "foo.bar"
    sample_schema["columns"][1]["name"] = "foo.baz"
    sample_schema["is_nested"] = is_nested

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json == [{'foo': {'bar': 'this', 'baz': 'that'}}] if is_nested \
        else res.json == [{'foo.bar': "this", "foo.baz": "that"}]


@pytest.mark.nested
@pytest.mark.schema
def test_nested_json_default(client: Eve, sample_schema: dict):
    """Test to ensure is_nested defaults to True

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["name"] = "foo.bar"
    sample_schema["columns"][1]["name"] = "foo.baz"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json == [{'foo': {'bar': 'this', 'baz': 'that'}}]


@pytest.mark.truncate
@pytest.mark.schema
@pytest.mark.parametrize('truncate', (True, False))
def test_truncate_column(client: Eve, sample_schema: dict, truncate: bool):
    """Test to ensure truncate is working

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :param bool truncate: Truncate column
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][1]["truncate"] = truncate

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert len(res.json) == sample_schema["num_rows"]
    assert 'bar' not in res.json[0] if truncate else 'bar' in res.json[0]


@pytest.mark.sql
@pytest.mark.schema
def test_sql_schema(client: Eve, sample_schema: dict):
    """Test to ensure SQL templating is working

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "sql"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/sql'

    # noinspection SqlResolve
    assert res.get_data() == b"INSERT INTO EXAMPLE_DATA (foo, bar) VALUES ('this', 'that');"


@pytest.mark.generate
@pytest.mark.schema
def test_generate_custom_schema(client: Eve, sample_schema: dict):
    """Test to ensure data can be generated for custom schemas

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'text/csv'
    assert res.get_data().decode('utf-8').count('\n') == sample_schema["num_rows"] + 1


@pytest.mark.generate
@pytest.mark.schema
def test_generate_date_format(client: Eve, sample_schema: dict):
    """Test to ensure dates can be formatted

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["type"] = "past_date"
    sample_schema["columns"][0]["args"] = {}
    sample_schema["columns"][0]["format"] = "%Y-%m-%d"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert datetime.strptime(res.json[0]["foo"], "%Y-%m-%d")


@pytest.mark.generate
@pytest.mark.schema
@pytest.mark.xfail(raises=ValueError)
def test_invalid_date_format(client: Eve, sample_schema: dict):
    """Test to ensure invalid dates raise ValueError

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["type"] = "past_date"
    sample_schema["columns"][0]["args"] = {}
    sample_schema["columns"][0]["format"] = "foo bar"

    client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})


@pytest.mark.generate
@pytest.mark.schema
def test_generate_without_type(client: Eve, sample_schema: dict):
    """Test to ensure columns without type default to empty

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    del sample_schema["columns"][0]["type"]
    del sample_schema["columns"][0]["args"]

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]["foo"] == ""


@pytest.mark.generate
@pytest.mark.schema
def test_generate_invalid_type(client: Eve, sample_schema: dict):
    """Test to ensure columns with invalid types default to empty

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0] = {"name": "foo", "type": "foobar"}

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]["foo"] == ""
