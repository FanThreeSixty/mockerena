"""mockerena.swagger

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""


from mockerena import __author__, __email__, __version__
from mockerena.settings import BASE_PATH, ENV, HOST, PORT
from mockerena.settings import DEFAULT_FILE_FORMAT, DEFAULT_INCLUDE_HEAD, DEFAULT_SIZE, DEFAULT_QUOTE_CHARACTER, \
    DEFAULT_EXCLUDE_NULL, DEFAULT_DELIMITER, DEFAULT_KEY_SEPARATOR, DEFAULT_IS_NESTED


TEMPLATE = {
    "swagger": "2.0",
    "info": {
        "title": "Mockerena API",
        "contact": {
            "name": __author__,
            "email": __email__
        },
        "version": __version__
    },
    "host": f"{HOST}:{PORT}" if HOST in ("localhost", "0.0.0.0") else HOST,
    "basePath": BASE_PATH,
    "schemes": ["http"] if ENV == 'development' else ["https"],
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json",
        "application/xml"
    ],
    "paths": {
        "/api/schema": {
            "get": {
                "summary": "Retrieves one or more schema",
                "responses": {
                    "200": {
                        "description": "An array of schema",
                        "schema": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/schema"
                            }
                        }
                    },
                    "301": {
                        "$ref": "#/responses/movedPermanently"
                    },
                    "500": {
                        "$ref": "#/responses/internalServerError"
                    }
                },
                "parameters": [
                    {
                        "$ref": "#/parameters/projection"
                    }
                ],
                "tags": [
                    "schema"
                ]
            },
            "post": {
                "summary": "Stores one or more schema",
                "parameters": [
                    {
                        "in": "body",
                        "name": "schema",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/schema"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "operation has been successful"
                    },
                    "301": {
                        "$ref": "#/responses/movedPermanently"
                    },
                    "500": {
                        "$ref": "#/responses/internalServerError"
                    }
                },
                "tags": [
                    "schema"
                ]
            }
        },
        "/api/schema/{schema_id}": {
            "get": {
                "summary": "Retrieves a schema document",
                "responses": {
                    "200": {
                        "description": "schema document fetched successfully",
                        "schema": {
                            "$ref": "#/definitions/schema"
                        }
                    },
                    "301": {
                        "$ref": "#/responses/movedPermanently"
                    },
                    "404": {
                        "$ref": "#/responses/notFound"
                    },
                    "500": {
                        "$ref": "#/responses/internalServerError"
                    }
                },
                "parameters": [
                    {
                        "$ref": "#/parameters/schema_id"
                    }
                ],
                "tags": [
                    "schema"
                ]
            },
            "put": {
                "summary": "Replaces a schema document",
                "responses": {
                    "200": {
                        "description": "schema document replaced successfully"
                    },
                    "301": {
                        "$ref": "#/responses/movedPermanently"
                    },
                    "404": {
                        "$ref": "#/responses/notFound"
                    },
                    "500": {
                        "$ref": "#/responses/internalServerError"
                    }
                },
                "parameters": [
                    {
                        "$ref": "#/parameters/schema_id"
                    },
                    {
                        "in": "body",
                        "name": "schema",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/schema"
                        }
                    },
                    {
                        "in": "header",
                        "name": "If-Match",
                        "description": "Current value of the _etag field",
                        "required": True,
                        "type": "string"
                    }
                ],
                "tags": [
                    "schema"
                ]
            },
            "patch": {
                "summary": "Updates a schema document",
                "responses": {
                    "200": {
                        "description": "schema document updated successfully"
                    },
                    "301": {
                        "$ref": "#/responses/movedPermanently"
                    },
                    "404": {
                        "$ref": "#/responses/notFound"
                    },
                    "500": {
                        "$ref": "#/responses/internalServerError"
                    }
                },
                "parameters": [
                    {
                        "$ref": "#/parameters/schema_id"
                    },
                    {
                        "in": "body",
                        "name": "schema",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/schema"
                        }
                    },
                    {
                        "in": "header",
                        "name": "If-Match",
                        "description": "Current value of the _etag field",
                        "required": True,
                        "type": "string"
                    }
                ],
                "tags": [
                    "schema"
                ]
            },
            "delete": {
                "summary": "Deletes a schema document",
                "responses": {
                    "204": {
                        "description": "schema document deleted successfully"
                    },
                    "301": {
                        "$ref": "#/responses/movedPermanently"
                    },
                    "404": {
                        "$ref": "#/responses/notFound"
                    },
                    "500": {
                        "$ref": "#/responses/internalServerError"
                    }
                },
                "parameters": [
                    {
                        "$ref": "#/parameters/schema_id"
                    },
                    {
                        "in": "header",
                        "name": "If-Match",
                        "description": "Current value of the _etag field",
                        "required": True,
                        "type": "string"
                    }
                ],
                "tags": [
                    "schema"
                ]
            }
        },
        "/environment": {
            "get": {
                "summary": "Retrieves environment information for service",
                "responses": {
                    "200": {
                        "description": "environment information",
                        "schema": {
                            "$ref": "#/definitions/environment"
                        }
                    }
                },
                "tags": [
                    "environment"
                ]
            }
        },
        "/healthcheck": {
            "get": {
                "summary": "Retrieves health information for service",
                "responses": {
                    "200": {
                        "description": "services are up",
                        "schema": {
                            "$ref": "#/definitions/healthcheck"
                        }
                    },
                    "500": {
                        "description": "services are down",
                        "schema": {
                            "$ref": "#/definitions/healthcheck"
                        }
                    }
                },
                "tags": [
                    "health"
                ]
            }
        }
    },
    "definitions": {
        "schema": {
            "type": "object",
            "properties": {
                "schema": {
                    "minLength": 3,
                    "maxLength": 64,
                    "type": "string",
                    "description": "Name of the schema"
                },
                "num_rows": {
                    "default": DEFAULT_SIZE,
                    "minimum": 1,
                    "type": "integer",
                    "description": "Number of records to generate"
                },
                "file_format": {
                    "enum": [
                        "csv",
                        "tsv",
                        "xml",
                        "html",
                        "json",
                        "sql"
                    ],
                    "type": "string",
                    "default": DEFAULT_FILE_FORMAT,
                    "description": "Type of file to output"
                },
                "file_name": {
                    "minLength": 3,
                    "maxLength": 64,
                    "type": "string",
                    "description": "Download file name. Can use '{}' as a placeholder for the datetime"
                },
                "include_header": {
                    "type": "boolean",
                    "default": DEFAULT_INCLUDE_HEAD,
                    "description": "True, to include header for CSV or TSV. Default is True"
                },
                "exclude_null": {
                    "type": "boolean",
                    "default": DEFAULT_EXCLUDE_NULL,
                    "description": "If False, null values are squashed for JSON formats"
                },
                "delimiter": {
                    "type": "string",
                    "default": DEFAULT_DELIMITER,
                    "description": "CSV column separator"
                },
                "quote_character": {
                    "type": "string",
                    "default": DEFAULT_QUOTE_CHARACTER,
                    "description": "Quoting character for CSV or TSV"
                },
                "is_nested": {
                    "type": "boolean",
                    "default": DEFAULT_IS_NESTED,
                    "description": "True, to generate JSON with nested columns. Dot-separate names to nest columns"
                },
                "key_separator": {
                    "type": "string",
                    "default": DEFAULT_KEY_SEPARATOR,
                    "description": "Character separator for generating nested JSON output"
                },
                "template": {
                    "type": "string",
                    "description": "HTML, XML or SQL template"
                },
                "columns": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "type": {
                                "type": "string",
                                "description": "Faker data type. See `/api/types` for a list of all types"
                            },
                            "name": {
                                "type": "string",
                                "description": "Column header name"
                            },
                            "format": {
                                "type": "string",
                                "description": "Date format"
                            },
                            "args": {
                                "type": "object",
                                "description": "Arguments passed into type"
                            },
                            "percent_empty": {
                                "minimum": 0,
                                "maximum": 1,
                                "type": "number",
                                "format": "float",
                                "description": "Likeliness that the column will be empty"
                            },
                            "truncate": {
                                "type": "boolean",
                                "default": False,
                                "description": "True, to exclude the column. Default is False"
                            },
                            "function": {
                                "type": "string",
                                "description": "Post-processing function"
                            },
                            "description": {
                                "type": "string",
                                "description": "A description of what what the column is for"
                            }
                        }
                    }
                },
                "_id": {
                    "type": "string",
                    "format": "objectid"
                }
            },
            "required": [
                "schema",
                "file_name"
            ]
        },
        "environment": {
            "type": "object",
            "properties": {
                "os": {
                    "type": "object",
                    "properties": {
                        "platform": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        },
                        "uname": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    },
                    "required": [
                        "platform",
                        "name",
                        "uname"
                    ]
                },
                "application": {
                    "type": "object",
                    "properties": {
                        "version": {
                            "type": "string"
                        },
                        "maintainer": {
                            "type": "string"
                        },
                        "maintainer_email": {
                            "type": "string"
                        },
                        "git_repo": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "version",
                        "maintainer",
                        "maintainer_email",
                        "git_repo"
                    ]
                },
                "settings": {
                    "type": "object",
                    "properties": {
                        "DEFAULT_FILE_FORMAT": {
                            "type": "string"
                        },
                        "DEFAULT_INCLUDE_HEAD": {
                            "type": "string"
                        },
                        "DEFAULT_SIZE": {
                            "type": "integer"
                        },
                        "DEFAULT_QUOTE_CHARACTER": {
                            "type": "string"
                        },
                        "DEFAULT_EXCLUDE_NULL": {
                            "type": "boolean"
                        },
                        "DEFAULT_DELIMITER": {
                            "type": "string"
                        },
                        "DEFAULT_KEY_SEPARATOR": {
                            "type": "string"
                        },
                        "DEFAULT_IS_NESTED": {
                            "type": "boolean"
                        },
                        "DEFAULT_RESPONSES": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "status_code": {
                                        "type": "integer"
                                    }
                                },
                                "required": [
                                    "status_code"
                                ]
                            }
                        }
                    },
                    "required": [
                        "DEFAULT_FILE_FORMAT",
                        "DEFAULT_INCLUDE_HEAD",
                        "DEFAULT_SIZE",
                        "DEFAULT_QUOTE_CHARACTER",
                        "DEFAULT_EXCLUDE_NULL",
                        "DEFAULT_DELIMITER",
                        "DEFAULT_KEY_SEPARATOR",
                        "DEFAULT_IS_NESTED",
                        "DEFAULT_RESPONSES"
                    ]
                }
            },
            "required": [
                "os",
                "application",
                "settings"
            ]
        },
        "healthcheck": {
            "type": "object",
            "properties": {
                "hostname": {
                    "type": "string"
                },
                "status": {
                    "type": "string"
                },
                "timestamp": {
                    "type": "number"
                },
                "results": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "checker": {
                                "type": "string"
                            },
                            "output": {
                                "type": "string"
                            },
                            "passed": {
                                "type": "boolean"
                            },
                            "timestamp": {
                                "type": "number"
                            },
                            "expires": {
                                "type": "number"
                            },
                            "response_time": {
                                "type": "number"
                            }
                        },
                        "required": [
                            "checker",
                            "output",
                            "passed",
                            "timestamp",
                            "expires",
                            "response_time"
                        ]
                    }
                },
                "version": {
                    "type": "string"
                }
            },
            "required": [
                "hostname",
                "status",
                "timestamp",
                "results",
                "version"
            ]
        },
        "notFound": {
            "type": "object",
            "properties": {
                "_status": {
                    "type": "string",
                    "default": "ERR"
                },
                "_error": {
                    "type": "object",
                    "properties": {
                        "code": {
                            "type": "integer",
                            "default": 404
                        },
                        "message": {
                            "type": "string",
                            "default": "The requested URL was not found on the server.  If you entered the URL "
                                       "manually please check your spelling and try again."
                        }
                    }
                }
            }
            }
    },
    "parameters": {
        "schema_id": {
            "in": "path",
            "name": "schema_id",
            "required": True,
            "type": "string",
            "format": "objectid"
        },
        "projection": {
            "in": "query",
            "name": "projection",
            "description": "Conditional query where the user dictates which fields should be returned by the API",
            "required": False,
            "type": "object",
            "example": '{"schema": 1}'
        },
        "file_format": {
            "in": "query",
            "name": "file_format",
            "description": "Format of output",
            "type": "string",
            "required": False,
            "default": DEFAULT_FILE_FORMAT,
            "enum": ["csv", "tsv", "json", "xml", "html"]
        },
        "numrows": {
            "in": "query",
            "name": "numrows",
            "description": "The number or rows of data to generate",
            "type": "int",
            "default": DEFAULT_SIZE,
            "required": False
        },
        "seed": {
            "in": "query",
            "name": "seed",
            "description": "The seed to use for the data generator",
            "required": False,
            "type": "int"
        },
        "include_header": {
            "in": "query",
            "name": "include_header",
            "description": "Include header with CSV, TSV or template",
            "required": False,
            "default": DEFAULT_INCLUDE_HEAD,
            "type": "boolean"
        },
        "exclude_null": {
            "in": "query",
            "name": "exclude_null",
            "description": "Squash nulls for JSON output",
            "required": False,
            "default": DEFAULT_EXCLUDE_NULL,
            "type": "boolean"
        },
        "If-Match": {
            "in": "header",
            "name": "If-Match",
            "description": "Current value of the _etag field",
            "required": True,
            "type": "string"
        }
    },
    "responses": {
        "movedPermanently": {
            "description": "Route does not support 'http'"
        },
        "preconditionFailed": {
            "description": "If-Match header must match etag"
        },
        "internalServerError": {
            "description": "The server encountered an internal error and was unable to complete your request. "
                           "Either the server is overloaded or there is an error in the application."
        },
        "notFound": {
            "description": "Resource was not found",
            "schema": {
                "$ref": "#/definitions/notFound"
            }

        }
    },
    "tags": [
        {
            "name": "schema"
        },
        {
            "name": "generate"
        },
        {
            "name": "health"
        },
        {
            "name": "environment"
        }
    ]
}
