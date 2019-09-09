"""Definition for mockerena schema

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

SCHEMA = {
    "item_title": "schema",
    "schema": {
        "schema": {
            "type": "string",
            "minlength": 3,
            "maxlength": 64,
            "unique": True,
            "required": True
        },
        "num_rows": {
            "type": "integer",
            "min": 1,
            "default": 1000
        },
        "file_format": {
            "type": "string",
            "allowed": ["csv", "tsv", "xml", "html", "json"]
        },
        "file_name": {
            "type": "string",
            "minlength": 3,
            "maxlength": 64,
            "unique": True,
            "required": True
        },
        "include_header": {"type": "boolean"},
        "include_null": {"type": "boolean"},
        "delimiter": {"type": "string"},
        "quote_character": {"type": "string"},
        "template": {
            "type": "string"
        },
        "columns": {
            "type": "list",
            "schema": {
                "type": "dict",
                "schema": {
                    "type": {"type": "string"},
                    "name": {"type": "string"},
                    "format": {"type": "string"},
                    "args": {"type": "dict"},
                    "percent_empty": {
                        "type": "float",
                        "min": 0,
                        "max": 1
                    },
                    "truncate": {"type": "boolean"},
                    "function": {"type": "string"},
                    "description": {"type": "string"}
                }
            }
        }
    },
    'additional_lookup': {
        'url': 'regex("[\\w]+")',
        'field': 'schema'
    },
}
