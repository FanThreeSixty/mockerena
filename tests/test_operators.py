"""test_operators

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from flask import url_for
import pytest


@pytest.mark.operators
@pytest.mark.parametrize('function,result', [
    ("1 + 1", 2),
    ("1 - 1", 0),
    ("2 * 3", 6),
    ("6 / 3", 2),
    ("7 // 3", 2),
    ("2 ** 2", 4),
    ("7 % 3", 1),
    ("1 == 1", True),
    ("2 != 1", True),
    ("1 > 2", False),
    ("6 < 3", False),
    ("3 >= 3", True),
    ("5 <= 4", False),
    ("1 is 1", True),
    ("not True", False),
    ("True and False", False),
    ("False or True", True),
    ("2 in range(1, 10)", True)
])
def test_operators(client, sample_schema, function, result):
    """Test to ensure all operators are accepted

    :param Flask client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :param str function: Column function
    :param int result: Function result
    :return:
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = function

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == result
