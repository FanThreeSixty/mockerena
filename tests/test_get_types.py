"""test_get_types

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from flask import url_for
import pytest


@pytest.mark.params
@pytest.mark.get_types
def test_get_types(client):
    """Test to ensure that types can be retrieved

    :param Flask client: Mockerena app instance
    :return:
    """

    res = client.get(url_for('get_types'))

    assert res.status_code == 200
    assert res.mimetype == 'application/json'
