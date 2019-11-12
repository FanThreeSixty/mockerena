"""test_responses

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

import datetime
from eve import Eve
from flask import url_for
import pytest


@pytest.mark.responses
def test_response_override_status_code(client: Eve, sample_schema: dict):
    """Test to ensure status code can be overridden on a response

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["responses"] = [{"status_code": 201}]

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 201


@pytest.mark.responses
def test_response_override_data(client: Eve, sample_schema: dict):
    """Test to ensure data can be overridden on a response

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["responses"] = [{"data": '{"status": "ok"}', "content_type": "application/json"}]

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json == {"status": "ok"}


@pytest.mark.responses
def test_response_override_content_type(client: Eve, sample_schema: dict):
    """Test to ensure content type can be overridden on a response

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["responses"] = [{"content_type": "application/xml"}]

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/xml'


@pytest.mark.responses
def test_response_custom_header(client: Eve, sample_schema: dict):
    """Test to ensure headers can be overridden on a response

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["responses"] = [{"headers": {"Last-Modified": "Thur, 19 Sep 2019 19:25:10 GMT"}}]

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})

    assert res.status_code == 200
    assert res.last_modified == datetime.datetime(2019, 9, 19, 19, 25, 10)
