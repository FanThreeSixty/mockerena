===============
Using Mockerena
===============

To generate fake data you can either:

1) save schemas and generate data using an id or
2) you can generate data on-the-fly.


To save a schema, POST to ``/api/schema``:

.. code-block:: json

    {
        "schema": "mock_example",
        "num_rows": 10,
        "file_format": "csv",
        "file_name": "mock_{}_example",
        "include_header": true,
        "delimiter": ",",
        "quote_character": "'",
        "columns": [
            {
                "name": "foo",
                "truncate": false,
                "type": "word",
                "description": "First column",
                "percent_empty": 0.2
            },
            {
                "name": "bar",
                "type": "random_element",
                "description": "Second column",
                "truncate": false,
                "args": {
                    "elements": ["that"]
                },
                "function": "this + this"
            }
        ]
    }

To breakdown what is happening at the schema-level above, here are what each item means:

    *schema* - The name of the schema

    *num_rows* - The default number of records to return

    *file_format* - The default format of the file

    *file_name* - The name of the file that is generated. `{}` is used to insert a datetime

    *include_header* - Include the header for the CSV

    *delimiter* - CSV column separator

    *quote_character* - Quoting character for CSV or TSV

On a column-level:

    *name* - Column header name

    *type* - Faker data type. See ``/api/types`` for a list of all types

    *description* - A description of what what the column is for

    *truncate* - Drop column after generation

    *percent_empty* - Likeliness that the column will be empty. 0 to 1, 1 being 100%

    *args* - Arguments passed into type

    *function* - Post-processing function (`see below <#functions>`_)


To generate data, GET to ``/api/schema/{schema_id}/generate``. You should receive something like this:

.. code-block:: text

    foo,bar
    lose,thatthat
    now,thatthat
    and,thatthat
    ,thatthat
    such,thatthat
    government,thatthat
    around,thatthat
    room,thatthat
    behind,thatthat
    television,thatthat

You can optionally POST to ``/api/schema/generate`` directly to generate data without having to permanently save the schema.

---------
Functions
---------


Mockerena mostly uses ``Faker`` providers to generate random data.
`Click here <https://faker.readthedocs.io/en/master/providers.html>`_ for the full list of providers from ``Faker``.
With Mockerena, we've supplied a few additional providers that are available `here <https://mockerena.readthedocs.io/en/latest/source/mockerena.html#module-mockerena.providers>`_.

You can also use the types endpoint ``/api/types`` to retrieve a complete list of all provider types.
