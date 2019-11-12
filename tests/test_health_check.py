"""test_health_check

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from flask import url_for
from eve import Eve
import pytest


@pytest.mark.health_check
def test_health_check(client: Eve):
    """Test health check route

    :param Eve client: Mockerena app instance
    :raises: AssertionError
    """

    res = client.get(url_for('healthcheck'))
    assert res.status_code == 200
    assert res.mimetype == 'application/json'

    data = res.json
    assert data['hostname']
    assert data['status']
    assert data['timestamp']
    assert data['results']
    assert data['version']
