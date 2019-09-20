===============
Using Mockerena
===============

To generate fake data you can either:

1) Save schemas and generate data using an id or
2) You can generate data on-the-fly.


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

    **schema** - The name of the schema

    **num_rows** - The default number of records to return

    **file_format** - The default format of the file

    **file_name** - The name of the file that is generated. `{}` is used to insert a datetime

    **include_header** - Include the header for the CSV

    **delimiter** - CSV column separator

    **quote_character** - Quoting character for CSV or TSV

On a column-level:

    **name** - Column header name

    **type** - Faker data type. See ``/api/types`` for a list of all types

    **description** - A description of what what the column is for

    **truncate** - Drop column after generation

    **percent_empty** - Likeliness that the column will be empty. 0 to 1, 1 being 100%

    **args** - Arguments passed into type

    **function** - Post-processing function (`see below <#functions>`_)


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

---------
Responses
---------

*Added v1.1.0*

Responses allow for custom responses to be randomly returned For example:

.. code-block:: JSON

    {
        "schema": "mock_example",
        "file_format": "csv",
        "file_name": "mock_{}_example",
        "columns": [
            {
                "name": "foo",
                "type": "word"
            }
        ],
        "responses": [
            {
                "status_code": 201,
                "weight": 2
            },
            {
                "status_code": 502,
                "data": "",
                "content_type": "text/plain",
                "headers": {
                    "Last-Modified": "Thur, 19 Sep 2019 19:25:10 GMT"
                },
                "weight": 1
            }
        ]
    }

To breakdown what is happening:

    **status_code** - Override response code returned. Default is 200

    **data** - Override data returned. Default is usual dataset

    **content_type** - Override content type. Default is based off *file_format*, or "*text/plain*"

    **headers** - Override response headers

    **weight** - Probability response is returned. For example, a response with a weight of 2 is twice as likely to return
    than a response with a weight of 1

So in the example approximately 2 out of 3 attempts will return the normal response with a status code of *201*,
but 1 out of 3 attempts will return a response with a status code of *502*, empty content and a last modified header
with the timestamp "*Thur, 19 Sep 2019 19:25:10 GMT*".
