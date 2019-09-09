"""test_example

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from flask import url_for
import pytest


@pytest.mark.example
def test_example(client):
    """Example test for reference

    :param Flask client: Mockerena app instance
    :return:
    """

    res = client.get(url_for('generate', schema_id='mock_example'))
    assert res.status_code == 200
    assert res.mimetype == 'text/csv'
