"""test_provider_integration

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from flask import url_for
import pytest


@pytest.mark.price
@pytest.mark.provider
def test_provider_price(client, sample_schema):
    """Test to ensure data can be generated for price

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["type"] = "price"
    sample_schema["columns"][0]["args"] = {"minimum": 1, "maximum": 100}

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert isinstance(res.json[0]['foo'], float)


@pytest.mark.regex
@pytest.mark.provider
def test_provider_regex(client, sample_schema):
    """Test to ensure data can be generated for regex

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["type"] = "regex"
    sample_schema["columns"][0]["args"] = {"expression": "foo|bar"}

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] in ('foo', 'bar')


@pytest.mark.regex
@pytest.mark.provider
def test_provider_weighted_choice(client, sample_schema):
    """Test to ensure data can be generated for weighted choice

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
    """

    sample_schema["file_format"] = "json"
    sample_schema["num_rows"] = 100
    sample_schema["columns"][0]["type"] = "weighted_choice"
    sample_schema["columns"][0]["args"] = {"elements": ["foo", "bar"], "weights": [2, 1]}

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'

    column_foo = list(map(lambda col: col["foo"], res.json))
    assert column_foo.count("foo") > column_foo.count("bar")


@pytest.mark.empty
@pytest.mark.provider
def test_provider_empty(client, sample_schema):
    """Test to ensure that empty returns an empty string

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :return:
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["type"] = "empty"
    sample_schema["columns"][0]["args"] = {}

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == ""
