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
from eve import Eve
from faker.providers import BaseProvider
from flasgger import Swagger, swag_from
from flask import request, render_template

from mockerena.errors import ERROR_404, ERROR_422
from mockerena.format import format_output
from mockerena.generate import fake, generate_data
from mockerena.settings import DEBUG, ENV, HOST, PORT, SECRET_KEY
from mockerena.swagger import TEMPLATE


app = Eve(__name__, settings=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.py'))
swagger = Swagger(app, template=TEMPLATE)
app.config.update(ENV=ENV, DEBUG=DEBUG, SECRET_KEY=SECRET_KEY)


def get_provider_types() -> dict:
    """Returns all available generator types

    :return:
    """

    def is_generator(method):
        return inspect.ismethod(method) and issubclass(type(method.__self__), BaseProvider)

    return {gen[0]: inspect.getdoc(gen[1]) for gen in inspect.getmembers(fake, predicate=is_generator)}


def generate_and_format(schema):
    """Generate and return formatted data

    :param schema:
    :return:
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

    mock_data = generate_data(schema)
    return format_output(mock_data, schema)


@app.before_request
def seed():
    """Seed Faker random generator

    :return:
    """

    fake.seed(request.args.get('seed'))


@app.route("/")
def index():
    """Test route to make sure everything is running

    :return:
    """

    return render_template('index.html')


@swag_from('swagger/generate.yml')
@app.route("/api/schema/<schema_id>/generate")
def generate(schema_id: str):
    """Generates sample data from a schema

    :param str schema_id: Schema id
    :return:
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
def custom_schema():
    """Generates sample data for the provided schema
    """

    return generate_and_format(request.get_json())


@swag_from('swagger/types.yml')
@app.route("/api/types")
def get_types() -> tuple:
    """Returns all available generator types

    :return:
    """

    return json.dumps(get_provider_types()), 200, {'Content-Type': 'application/json'}


if __name__ != '__main__':  # pragma: no cover
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    logging.basicConfig(level=gunicorn_logger.level)


if __name__ == "__main__":  # pragma: no cover
    app.run(host=HOST, debug=DEBUG, port=PORT)
