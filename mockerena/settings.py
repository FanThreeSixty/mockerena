"""Mockerena eve settings
"""

import os
from mockerena.models.schema import SCHEMA


URL_PREFIX = 'api'
DOMAIN = {'schema': SCHEMA}

HOST = os.environ.get('MOCKERENA_HOST', 'localhost')
PORT = os.environ.get('MOCKERENA_PORT', 9000)
BASE_PATH = os.environ.get('MOCKERENA_BASE_PATH', '')
DEBUG = os.environ.get('MOCKERENA_DEBUG', False)
SECRET_KEY = os.environ.get('MOCKERENA_SECRET_KEY', None)
ENV = os.environ.get('MOCKERENA_ENV', 'development')

RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# Database settings
MONGO_HOST = os.environ.get('MOCKERENA_MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MOCKERENA_MONGO_PORT', 27017)
MONGO_DBNAME = os.environ.get('MOCKERENA_MONGO_DBNAME', 'mockerena')
MONGO_AUTH_SOURCE = os.environ.get('MOCKERENA_MONGO_AUTH_SOURCE', 'mockerena')
MONGO_USERNAME = os.environ.get('MOCKERENA_MONGO_USERNAME', '')
MONGO_PASSWORD = os.environ.get('MOCKERENA_MONGO_PASSWORD', '')


# Project defaults
DEFAULT_FILE_FORMAT = 'csv'
DEFAULT_INCLUDE_HEAD = True
DEFAULT_SIZE = 100
DEFAULT_QUOTE_CHARACTER = '"'
DEFAULT_EXCLUDE_NULL = False
DEFAULT_DELIMITER = None
DEFAULT_KEY_SEPARATOR = '.'
DEFAULT_IS_NESTED = True
DEFAULT_RESPONSES = [{"status_code": 200}]
