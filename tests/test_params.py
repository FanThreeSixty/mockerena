"""test_params

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from eve import Eve
from flask import url_for
import pytest


@pytest.mark.params
@pytest.mark.num_rows
def test_num_rows(client: Eve):
    """Test to ensure number of rows can be overridden

    :param Eve client: Mockerena app instance
    :raises: AssertionError
    """

    res = client.get(url_for('generate', schema_id='mock_example'), query_string={'numrows': 100})
    assert res.status_code == 200
    assert res.mimetype == 'text/csv'
    assert res.get_data().decode('utf-8').count('\n') == 101  # Includes header (+1)


@pytest.mark.params
@pytest.mark.include_header
def test_include_header(client: Eve):
    """Test to ensure include header can be overridden

    :param Eve client: Mockerena app instance
    :raises: AssertionError
    """

    url = url_for('generate', schema_id='mock_example')
    res = client.get(url, query_string={'include_header': 'false'})

    assert res.status_code == 200
    assert res.mimetype == 'text/csv'
    assert res.get_data().decode('utf-8').count('\n') == 10  # Omits header


@pytest.mark.params
@pytest.mark.file_format
def test_file_format(client: Eve):
    """Test to ensure file format can be overridden

    :param Eve client: Mockerena app instance
    :raises: AssertionError
    """

    url = url_for('generate', schema_id='mock_example')
    res = client.get(url, query_string={'file_format': 'json'})

    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert res.json
