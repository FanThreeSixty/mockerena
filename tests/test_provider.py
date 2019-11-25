"""test_provider_integration

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from typing import Union
from eve import Eve
from flask import url_for
import pytest


@pytest.mark.price
@pytest.mark.provider
def test_provider_price(client: Eve, sample_schema: dict):
    """Test to ensure data can be generated for price

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["type"] = "price"
    sample_schema["columns"][0]["args"] = {"minimum": 1, "maximum": 100}

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert isinstance(res.json[0]['foo'], float)


@pytest.mark.price
@pytest.mark.provider
@pytest.mark.parametrize('min_', (1, 'a'))
@pytest.mark.parametrize('max_', (100, 'b'))
def test_provider_price_invalid(client: Eve, sample_schema: dict, min_: Union[int, str], max_: Union[int, str]):
    """Test to ensure price defaults invalid inputs

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :param Union[str, int] min_: Minimum value
    :param Union[str, int] max_: Maximum value
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["type"] = "price"
    sample_schema["columns"][0]["args"] = {"minimum": min_, "maximum": max_}

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert isinstance(res.json[0]['foo'], float)


@pytest.mark.price
@pytest.mark.provider
def test_provider_price_negative(client: Eve, sample_schema: dict):
    """Test to ensure price defaults invalid inputs

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["type"] = "price"
    sample_schema["columns"][0]["args"] = {"minimum": -100, "maximum": -1}

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert isinstance(res.json[0]['foo'], float)
    assert res.json[0]['foo'] < 0


@pytest.mark.regex
@pytest.mark.provider
def test_provider_regex(client: Eve, sample_schema: dict):
    """Test to ensure data can be generated for regex

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
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
def test_provider_regex_invalid(client: Eve, sample_schema: dict):
    """Test to ensure regex defaults invalid inputs

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["type"] = "regex"
    sample_schema["columns"][0]["args"] = {"expression": 100}

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == ''


@pytest.mark.regex
@pytest.mark.provider
def test_provider_weighted_choice(client: Eve, sample_schema: dict):
    """Test to ensure data can be generated for weighted choice

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
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


@pytest.mark.regex
@pytest.mark.provider
@pytest.mark.parametrize('elements, weights', (
        (1, 2),
        (('foo', 'bar'), 3),
        (4, (5, 6)),
        (('foo', 'bar', 'baz'), (1, 2)),
        (('foo', 'bar'), (1, 2, 3))
))
def test_provider_weighted_choice_invalid(client: Eve, sample_schema: dict, elements: tuple, weights: tuple):
    """Test to invalid inputs raise an assertion error

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :param tuple elements: Elements to choose from
    :param tuple weights: Weights to give each element
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["num_rows"] = 100
    sample_schema["columns"][0]["type"] = "weighted_choice"
    sample_schema["columns"][0]["args"] = {"elements": elements, "weights": weights}

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 400


@pytest.mark.empty
@pytest.mark.provider
def test_provider_empty(client: Eve, sample_schema: dict):
    """Test to ensure that empty returns an empty string

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["type"] = "empty"
    sample_schema["columns"][0]["args"] = {}

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == ""
