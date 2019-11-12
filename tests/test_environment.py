"""test_environment

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from flask import url_for
from eve import Eve
import pytest


@pytest.mark.environment
def test_environment(client: Eve):
    """Test environment route

    :param Eve client: Mockerena app instance
    :raises: AssertionError
    """

    res = client.get(url_for('environment'))
    assert res.status_code == 200
    assert res.mimetype == 'application/json'

    data = res.json
    assert data['os']
    assert data['application']
    assert data['settings']
