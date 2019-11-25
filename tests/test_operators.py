"""test_operators

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from typing import Any
from flask import url_for
from eve import Eve
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
def test_operators(client: Eve, sample_schema: dict, function: str, result: Any):
    """Test to ensure all operators are accepted

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :param str function: Column function
    :param Any result: Function result
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = function

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json[0]['foo'] == result


@pytest.mark.operators
@pytest.mark.parametrize('function', (
    "1 + None",
    "1 - None",
    "2 * None",
    "6 / 'a'",
    "6 / 0",
    "7 // 'a'",
    "2 ** 'a'",
    "7 % 'b'",
    "2 in 4",
))
def test_invalid_operators(client: Eve, sample_schema: dict, function: str):
    """Test to ensure all operators are accepted

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :param str function: Column function
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "json"
    sample_schema["columns"][0]["function"] = function

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 400
    assert res.mimetype == 'application/json'
