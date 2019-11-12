"""test_example

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from flask import url_for
from eve import Eve
import pytest


@pytest.mark.example
def test_example(client: Eve):
    """Example test for reference

    :param Eve client: Mockerena app instance
    :raises: AssertionError
    """

    res = client.get(url_for('generate', schema_id='mock_example'))
    assert res.status_code == 200
    assert res.mimetype == 'text/csv'
