"""test_get_types

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from flask import url_for
from eve import Eve
import pytest


@pytest.mark.params
@pytest.mark.get_types
def test_get_types(client: Eve):
    """Test to ensure that types can be retrieved

    :param Eve client: Mockerena app instance
    :raises: AssertionError
    """

    res = client.get(url_for('get_types'))

    assert res.status_code == 200
    assert res.mimetype == 'application/json'
