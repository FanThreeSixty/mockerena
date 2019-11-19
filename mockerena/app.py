#!/usr/bin/env python
"""Generate mock data for new integrations

.. codeauthor:: Michael Holtzscher <mholtzscher@fanthreesixty.com>
.. codeauthor:: Robert Langenfeld <rlangenfeld@fanthreesixty.com>
.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

import inspect
import json
import logging
import os

from bson.objectid import ObjectId
from cerberus import Validator
from eve import Eve
from faker.providers import BaseProvider
from flasgger import Swagger, swag_from
from flask import request, render_template
from healthcheck import HealthCheck, EnvironmentDump
from pymongo.errors import ServerSelectionTimeoutError

from mockerena import __author__, __email__, __version__
from mockerena.errors import ERROR_404, ERROR_422
from mockerena.format import format_output
from mockerena.generate import fake, generate_data
from mockerena.models.schema import CUSTOM_SCHEMA
from mockerena.settings import DEBUG, DEFAULT_FILE_FORMAT, DEFAULT_INCLUDE_HEAD, DEFAULT_SIZE, \
    DEFAULT_QUOTE_CHARACTER, DEFAULT_EXCLUDE_NULL, DEFAULT_DELIMITER, DEFAULT_KEY_SEPARATOR, \
    DEFAULT_IS_NESTED, DEFAULT_RESPONSES, ENV, HOST, PORT, SECRET_KEY
from mockerena.swagger import TEMPLATE


app = Eve(__name__, settings=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.py'))
envdump = EnvironmentDump(include_python=False, include_process=False)
health = HealthCheck()
swagger = Swagger(app, template=TEMPLATE)
app.config.update(ENV=ENV, DEBUG=DEBUG, SECRET_KEY=SECRET_KEY)


def application_data() -> dict:
    """Returns information about the application

    :return: A map of application information
    :rtype: dict
    """

    return {
        "version": __version__,
        "maintainer": __author__,
        "maintainer_email": __email__,
        "git_repo": "https://github.com/FanThreeSixty/mockerena"
    }


def application_settings() -> dict:
    """Returns application settings

    :return: A map of application settings
    :rtype: dict
    """

    return {
        "DEFAULT_FILE_FORMAT": DEFAULT_FILE_FORMAT,
        "DEFAULT_INCLUDE_HEAD": DEFAULT_INCLUDE_HEAD,
        "DEFAULT_SIZE": DEFAULT_SIZE,
        "DEFAULT_QUOTE_CHARACTER": DEFAULT_QUOTE_CHARACTER,
        "DEFAULT_EXCLUDE_NULL": DEFAULT_EXCLUDE_NULL,
        "DEFAULT_DELIMITER": DEFAULT_DELIMITER,
        "DEFAULT_KEY_SEPARATOR": DEFAULT_KEY_SEPARATOR,
        "DEFAULT_IS_NESTED": DEFAULT_IS_NESTED,
        "DEFAULT_RESPONSES": DEFAULT_RESPONSES
    }


def mongo_available() -> tuple:
    """Return status of mongo connection

    :return: Tuple with boolean and text status
    :rtype: tuple
    """

    try:
        app.data.driver.db.client.server_info()
        return True, "mongo up"
    except ServerSelectionTimeoutError:
        return False, "mongo down"


def get_provider_types() -> dict:
    """Returns all available generator types

    :return: Mapping of all generator types
    :rtype: dict
    """

    def is_generator(method):
        return inspect.ismethod(method) and issubclass(type(method.__self__), BaseProvider)

    return {gen[0]: inspect.getdoc(gen[1]) for gen in inspect.getmembers(fake, predicate=is_generator)}


def generate_and_format(schema: dict) -> tuple:
    """Generate and return formatted data

    :param dict schema:
    :return: A http response
    :rtype: tuple
    """

    if not isinstance(schema, dict):

        error = {
            "_status": "ERR",
            "_issues": {
                "validation exception": f"'{str(schema)}' is not a document, must be a dict"
            },
            "_error": ERROR_422
        }

        return json.dumps(error), 422, {'Content-Type': 'application/json'}

    num_rows = request.args.get('numrows', schema.get('num_rows', DEFAULT_SIZE))
    size = int(num_rows if str(num_rows).isnumeric() else DEFAULT_SIZE)

    return format_output(generate_data(schema, size), schema, size)


@app.before_request
def seed():
    """Seed Faker random generator
    """

    fake.seed(request.args.get('seed'))


@app.route("/")
def index() -> tuple:
    """Test route to make sure everything is running

    :return: A http response
    :rtype: tuple
    """

    return render_template('index.html')


@swag_from('swagger/generate.yml')
@app.route("/api/schema/<schema_id>/generate")
def generate(schema_id: str) -> tuple:
    """Generates sample data from a schema

    :param str schema_id: Schema id
    :return: A http response
    :rtype: tuple
    """

    search = [{'schema': schema_id}]

    if ObjectId.is_valid(schema_id):
        search.append({'_id': ObjectId(schema_id)})

    schema = app.data.driver.db['schema'].find_one({"$or": search})

    if not schema:
        return json.dumps({"_status": "ERR", "_error": ERROR_404}), 404, {'Content-Type': 'application/json'}

    return generate_and_format(schema)


@swag_from('swagger/custom_schema.yml')
@app.route("/api/schema/generate", methods=['POST'])
def custom_schema() -> tuple:
    """Generates sample data for the provided schema

    :return: A http response
    :rtype: tuple
    """

    validator = Validator(CUSTOM_SCHEMA)
    data = request.get_json()

    if not isinstance(data, dict) or not validator.validate(data):

        data_error = {"validation exception": f"'{str(data)}' is not a document, must be a dict"}

        error = {
            "_status": "ERR",
            "_issues": data_error if not isinstance(data, dict) else validator.errors,
            "_error": ERROR_422
        }

        return json.dumps(error), 422, {'Content-Type': 'application/json'}

    return generate_and_format(data)


@swag_from('swagger/types.yml')
@app.route("/api/types")
def get_types() -> tuple:
    """Returns all available generator types

    :return: A http response
    :rtype: tuple
    """

    return json.dumps(get_provider_types()), 200, {'Content-Type': 'application/json'}


# Add environment and health check routes
envdump.add_section("application", application_data)
envdump.add_section("settings", application_settings)
health.add_check(mongo_available)
health.add_section("version", __version__)
app.add_url_rule("/healthcheck", "healthcheck", view_func=health.run)
app.add_url_rule("/environment", "environment", view_func=envdump.run)


if __name__ != '__main__':  # pragma: no cover
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    logging.basicConfig(level=gunicorn_logger.level)


if __name__ == "__main__":  # pragma: no cover
    app.run(host=HOST, debug=DEBUG, port=PORT)
