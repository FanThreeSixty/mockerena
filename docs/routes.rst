==========
API Routes
==========


Retrieve all schemas
--------------------

    **GET** ``/api/schema``

    Retrieves one or more schema

    Query params (optional):

    +---------------------+--------------------------------------------------------------------------------------+
    | Parameter           | Description                                                                          |
    +=====================+======================================================================================+
    | *projection*        | Conditional query where the user dictates which fields should be returned by the API |
    +---------------------+--------------------------------------------------------------------------------------+


Store a schema
--------------

    **POST** ``/api/schema``

    Stores one or more schema


Retrieve a schema
-----------------

    **GET** ``/api/schema/{schema_id}``

    Retrieves a schema document

    +---------------+----------------------------------------------------------------------------------+
    | Parameter     | Description                                                                      |
    +===============+==================================================================================+
    | *schema_id*   | Either the name or the id of the schema                                          |
    +---------------+----------------------------------------------------------------------------------+


Replace a schema
----------------

    **PUT** ``/api/schema/{schema_id}``

    Replaces a schema document

    +---------------+----------------------------------------------------------------------------------+
    | Parameter     | Description                                                                      |
    +===============+==================================================================================+
    | *schema_id*   | Either the name or the id of the schema                                          |
    +---------------+----------------------------------------------------------------------------------+


Update a schema
---------------

    **PATCH** ``/api/schema/{schema_id}``

    Updates a schema document

    +---------------+----------------------------------------------------------------------------------+
    | Parameter     | Description                                                                      |
    +===============+==================================================================================+
    | *schema_id*   | Either the name or the id of the schema                                          |
    +---------------+----------------------------------------------------------------------------------+


Delete a schema
---------------

    **DELETE** ``/api/schema/{schema_id}``

    Deletes a schema document

    +---------------+----------------------------------------------------------------------------------+
    | Parameter     | Description                                                                      |
    +===============+==================================================================================+
    | *schema_id*   | Either the name or the id of the schema                                          |
    +---------------+----------------------------------------------------------------------------------+


Generate data
-------------

    **GET** ``/api/schema/generate``

    Generates sample data for a provided schema

    Query params (optional):

    +------------------+------------------------------------------+
    | Parameter        | Description                              |
    +==================+==========================================+
    | *seed*           | The seed to use for the data generator   |
    +------------------+------------------------------------------+
    | *numrows*        | The number or rows of data to generate   |
    +------------------+------------------------------------------+
    | *file_format*    | Format of output                         |
    +------------------+------------------------------------------+
    | *include_header* | Include header with CSV, TSV or template |
    +------------------+------------------------------------------+
    | *exclude_null*   | Squash nulls for JSON output             |
    +------------------+------------------------------------------+


Generate data
-------------

    **GET** ``/api/schema/{schema_id}/generate``

    Generates sample data from a schema

    +---------------+----------------------------------------------------------------------------------+
    | Parameter     | Description                                                                      |
    +===============+==================================================================================+
    | *schema_id*   | Either the name or the id of the schema                                          |
    +---------------+----------------------------------------------------------------------------------+

    Query params (optional):

    +------------------+------------------------------------------+
    | Parameter        | Description                              |
    +==================+==========================================+
    | *seed*           | The seed to use for the data generator   |
    +------------------+------------------------------------------+
    | *numrows*        | The number or rows of data to generate   |
    +------------------+------------------------------------------+
    | *file_format*    | Format of output                         |
    +------------------+------------------------------------------+
    | *include_header* | Include header with CSV, TSV or template |
    +------------------+------------------------------------------+
    | *exclude_null*   | Squash nulls for JSON output             |
    +------------------+------------------------------------------+

Get provider types
------------------

    **DELETE** ``/api/types``

    Returns all available provider types
