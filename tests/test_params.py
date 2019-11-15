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


@pytest.mark.params
@pytest.mark.exclude_null
@pytest.mark.parametrize('value,is_removed', (
        (True, True),
        ('true', True),
        ('t', True),
        ('yes', True),
        ('y', True),
        ('1', True),
        (False, False),
        ('false', False),
        ('f', False),
        ('no', False),
        ('n', False),
        ('0', False)
))
def test_exclude_null(client: Eve, sample_schema: dict, value: str, is_removed: bool):
    """Test to ensure exclude_null can be overridden

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :param str value: Include header value
    :param bool is_removed: Row count
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema['columns'][0]['percent_empty'] = 1
    res = client.post(url_for('custom_schema'), json=sample_schema, query_string={'exclude_null': value})

    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert 'foo' not in res.json[0] if is_removed else 'foo' in res.json[0]


@pytest.mark.params
@pytest.mark.include_header
def test_invalid_exclude_null(client: Eve, sample_schema: dict):
    """Test to ensure exclude_null defaults to false

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["file_format"] = "json"
    sample_schema['columns'][0]['percent_empty'] = 1
    res = client.post(url_for('custom_schema'), json=sample_schema, query_string={'exclude_null': 'foo'})

    assert res.status_code == 200
    assert res.mimetype == 'application/json'
    assert 'foo' in res.json[0]
