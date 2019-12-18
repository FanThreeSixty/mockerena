"""test_example

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""


from flask import url_for
from eve import Eve
import pytest
from mockerena.format import generate_xml_template


@pytest.mark.file_format
def test_generate_xml_template_flat():
    """Generate xml template should accept flat structure

    :raises: AssertionError
    """

    res = generate_xml_template({'bar': "{{ r['bar'] }}", 'baz': "{{ r['baz'] }}"}, 'foo')
    assert res == "<foo>{% for r in records %}<bar>{{ r['bar'] }}</bar><baz>{{ r['baz'] }}</baz>{% endfor %}</foo>"


@pytest.mark.file_format
def test_generate_xml_template_nested():
    """Generate xml template should accept nested structure

    :raises: AssertionError
    """

    res = generate_xml_template({'b': "{{ r['b'] }}", 'c': {'d': "{{ r['c.d'] }}"}}, 'a')
    assert res == "<a>{% for r in records %}<b>{{ r['b'] }}</b><c><d>{{ r['c.d'] }}</d></c>{% endfor %}</a>"


@pytest.mark.file_format
def test_generate_xml_template_empty_root():
    """Generate xml template should not render empty root nodes

    :raises: AssertionError
    """

    res = generate_xml_template({'foo': {'bar': "{{ r['bar'] }}"}, 'baz': "{{ r['baz'] }}"}, '')
    assert res == "{% for r in records %}<baz>{{ r['baz'] }}</baz><foo><bar>{{ r['bar'] }}</bar></foo>{% endfor %}"


@pytest.mark.file_format
def test_generate_xml_template_no_columns():
    """Generate xml template should not render if columns is empty

    :raises: AssertionError
    """

    res = generate_xml_template({}, '')
    assert res == ''


@pytest.mark.file_format
def test_generate_xml_data(client: Eve, sample_schema: dict):
    """Test to xml can be generated

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "xml"
    sample_schema["root_node"] = "custom"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.get_data().decode('utf-8') == '<custom><foo>this</foo><bar>that</bar></custom>'


@pytest.mark.file_format
def test_generate_xml_with_default_root(client: Eve, sample_schema: dict):
    """Test to xml can be generated without specifying a root

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "xml"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.get_data().decode('utf-8') == '<root><foo>this</foo><bar>that</bar></root>'


@pytest.mark.file_format
def test_generate_xml_with_nested(client: Eve, sample_schema: dict):
    """Test to xml can be generated with nested values

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "xml"
    sample_schema["is_nested"] = True
    sample_schema["columns"][0]["name"] = "foo.bar"
    sample_schema["columns"][1]["name"] = "foo.baz"

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.get_data().decode('utf-8') == '<root><foo><bar>this</bar><baz>that</baz></foo></root>'


@pytest.mark.file_format
def test_generate_xml_with_empty_root(client: Eve, sample_schema: dict):
    """Test to xml can be generated with an empty root

    :param Eve client: Mockerena app instance
    :param dict sample_schema: Sample schema data
    :raises: AssertionError
    """

    sample_schema["num_rows"] = 1
    sample_schema["file_format"] = "xml"
    sample_schema["root_node"] = ""

    res = client.post(url_for('custom_schema'), json=sample_schema, headers={'Content-Type': "application/json"})
    assert res.status_code == 200
    assert res.get_data().decode('utf-8') == '<foo>this</foo><bar>that</bar>'
