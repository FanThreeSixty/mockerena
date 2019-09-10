"""test_schemas

.. codeauthor:: Michael Holtzscher <mholtzscher@fanthreesixty.com>
.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from datetime import datetime
import pytest
from flask import url_for


@pytest.mark.schema
def test_get_all_schemas(client):
    """Tests that results are returned for get_all_schemas

    :param Flask client: Mockerena app instance
    :return:
    """

    res = client.get(url_for('schema|resource'))
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json


@pytest.mark.schema
def test_generate_by_schema_id(client):
    """Test to ensure a user can generate data for a schema by id

    :param Flask client: Mockerena app instance
    :return:
    """

    res = client.get(url_for('schema|item_lookup', _id='mock_example'))
    assert res.status_code == 200

    data = res.json

    res = client.get(url_for('generate', schema_id=data['_id']))
    assert res.status_code == 200
    assert res.mimetype == 'text/csv'


@pytest.mark.schema
def test_missing_generate_schema(client):
    """Test to ensure a missing schema returns a 500

    :param Flask client: Mockerena app instance
    :return:
    """

    message = "The requested URL was not found on the server.  If you entered the URL manually please " \
              "check your spelling and try again."

    res = client.get(url_for('generate', schema_id='foo_bar'))
    assert res.status_code == 404
    assert res.json["_status"] == "ERR"
    assert res.json["_error"]["code"] == 404
    assert res.json["_error"]["message"] == message


@pytest.mark.schema
def test_missing_schema(client):
    """Test to ensure a missing schema returns a 500

    :param Flask client: Mockerena app instance
    :return:
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
def test_malformed_schema(client):
    """Test to ensure the proper error returns for malformed input

    :param Flask client: Mockerena app instance
    :return:
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
def test_function_delimiter(client, sample_schema):
    """Test to ensure delimiter is working

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
    """

    sample_schema["delimiter"] = "|"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'text/csv'
    assert str(res.get_data()).count('|') == sample_schema["num_rows"] + 1


@pytest.mark.template
@pytest.mark.schema
def test_function_template(client, sample_schema):
    """Test to ensure template is working

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
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
def test_missing_template(client, sample_schema):
    """Test to ensure template is working

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
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
def test_nested_json(client, sample_schema):
    """Test to ensure template is working

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
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
def test_truncate_column(client, sample_schema):
    """Test to ensure truncate is working

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][1]["truncate"] = True

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert len(res.json) == sample_schema["num_rows"]
    assert 'bar' not in res.json[0]


@pytest.mark.sql
@pytest.mark.schema
def test_sql_schema(client, sample_schema):
    """Test to ensure SQL templating is working

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
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
def test_generate_custom_schema(client, sample_schema):
    """Test to ensure data can be generated for custom schemas

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
    """

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'text/csv'
    assert res.get_data().decode('utf-8').count('\n') == sample_schema["num_rows"] + 1


@pytest.mark.generate
@pytest.mark.schema
def test_generate_date_format(client, sample_schema):
    """Test to ensure dates can be formatted

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["type"] = "past_date"
    sample_schema["columns"][0]["args"] = {}
    sample_schema["columns"][0]["format"] = "%Y-%m-%d"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert datetime.strptime(res.json[0]["foo"], "%Y-%m-%d")