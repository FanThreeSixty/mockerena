"""test_seed

.. codeauthor:: Michael Holtzscher <mholtzscher@fanthreesixty.com>

"""

import pytest
from eve import Eve
from flask import url_for


@pytest.mark.seed
@pytest.mark.parametrize('seed', [
    42,
    50,
    23983745987345
])
def test_seed(client: Eve, seed: int, sample_schema: dict):
    """Tests seed query parameter working correctly

    :param Eve client: Mockerena app instance
    :param int seed: Seed to test
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    iterations = 1000
    sample_schema["columns"][0]["type"] = "word"
    sample_schema["columns"][0]["args"] = {}
    sample_schema["columns"][1]["type"] = "random_int"
    sample_schema["columns"][1]["args"] = {}

    results = [client.post(url_for('custom_schema', seed=seed), json=sample_schema).data for _ in range(iterations)]
    assert len(set(results)) == 1


@pytest.mark.seed
def test_no_seed(client: Eve, sample_schema: dict):
    """Tests not setting seed param generates unique data

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    iterations = 1000
    sample_schema["columns"][0]["type"] = "word"
    sample_schema["columns"][0]["args"] = {}
    sample_schema["columns"][1]["type"] = "random_int"
    sample_schema["columns"][1]["args"] = {}

    results = [client.post(url_for('custom_schema'), json=sample_schema).data for _ in range(iterations)]
    assert len(set(results)) == iterations
