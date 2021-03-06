"""Definition for mockerena schema

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

from copy import deepcopy


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
            "required": True
        },
        "file_name": {
            "type": "string",
            "minlength": 3,
            "maxlength": 64,
            "unique": True,
            "required": True
        },
        "include_header": {"type": "boolean"},
        "exclude_null": {"type": "boolean"},
        "is_nested": {"type": "boolean"},
        "delimiter": {"type": "string"},
        "key_separator": {"type": "string"},
        "quote_character": {"type": "string"},
        "template": {"type": "string"},
        "root_node": {"type": "string"},
        "table_name": {
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
        },
        "responses": {
            "type": "list",
            "items": [
                {
                    "type": "dict",
                    "schema": {
                        "status_code": {
                            "type": "integer",
                            "min": 100,
                            "max": 599
                        },
                        "headers": {"type": "dict", "allow_unknown": True},
                        "content_type": {"type": "string"},
                        "data": {"type": "string"},
                        "weight": {
                            "type": "integer",
                            "min": 1
                        }
                    }
                }
            ]
        }
    },
    "additional_lookup": {
        "url": 'regex("[\\w]+")',
        "field": "schema"
    },
}

# Build a schema for custom_schema route
CUSTOM_SCHEMA = deepcopy(SCHEMA["schema"])
del CUSTOM_SCHEMA["schema"]["unique"]
del CUSTOM_SCHEMA["file_name"]["unique"]
