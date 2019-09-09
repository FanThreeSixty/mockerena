"""test_example

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from flask import url_for
import pytest


@pytest.mark.index
def test_index(client):
    """To to ensure index page successfully returns

    :param Flask client: Mockerena app instance
    :return:
    """

    res = client.get(url_for('index'))
    assert res.status_code == 200
