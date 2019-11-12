"""test_example

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from flask import url_for
from eve import Eve
import pytest


@pytest.mark.index
def test_index(client: Eve):
    """To to ensure index page successfully returns

    :param Eve client: Mockerena app instance
    :raises: AssertionError
    """

    res = client.get(url_for('index'))
    assert res.status_code == 200
