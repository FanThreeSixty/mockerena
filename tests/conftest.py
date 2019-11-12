"""conftest.py

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from copy import deepcopy
from flask import url_for
from eve import Eve
import pytest
from mockerena.app import app as server


MOCK_SCHEMA = {
    "schema": "mock_example",
    "num_rows": 10,
    "file_format": "csv",
    "file_name": "mock_{}_example",
    "columns": [
        {
            "name": "foo",
            "type": "random_element",
            "args": {
                "elements": ["this"]
            }
        },
        {
            "name": "bar",
            "type": "random_element",
            "args": {
                "elements": ["that"]
            }
        }
    ]
}


@pytest.fixture(scope="session")
def app() -> Eve:
    """Returns mockerena app instance as a test fixture

    :return: An Eve application
    :rtype: Eve
    """

    return server


@pytest.fixture()
def sample_schema() -> dict:
    """Returns sample schema for mockerena

    :return: An example schema
    :rtype: dict
    """

    return deepcopy(MOCK_SCHEMA)


@pytest.fixture(autouse=True)
def setup_data(client):
    """Setup example schema for testing

    :param Flask client: Mockerena app instance
    """

    data = deepcopy(MOCK_SCHEMA)

    # Setup
    if not client.get(url_for('schema|item_lookup', _id='mock_example')).status_code == 200:
        client.post(url_for('schema|resource'), json=data, headers={'Content-Type': "application/json"})

    yield

    # Teardown
    if client.get(url_for('schema|item_lookup', _id='mock_example')).status_code == 200:
        client.delete(url_for('schema|item_lookup', _id='mock_example'))
