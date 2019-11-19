"""test_conversion

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from flask import url_for
from eve import Eve


def test_nan_conversion(client: Eve, sample_schema: dict):
    """Test to ensure nan is not returned from generate

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["percent_empty"] = 0.5
    sample_schema["columns"][0]["type"] = "random_int"
    del sample_schema["columns"][0]["args"]

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})

    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert b"NaN" not in res.data
