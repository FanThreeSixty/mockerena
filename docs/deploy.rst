==========
Deployment
==========

-------------
Deploy to AWS
-------------

First you'll need to install the AWS CLI and configure. For more information on these steps,
please visit `Amazon's documentation <https://docs.aws.amazon.com/transcribe/latest/dg/setup-asc-awscli.html>`_ for further details.
Once the CLI is installed you'll need to install the serverless cli:

.. code-block:: bash

    npm install -g serverless


Afterwards, to deploy simply run:

.. code-block:: bash

    serverless deploy


Once the deploy is complete, run ``sls info`` to get the endpoint:

.. code-block:: bash

    sls info

-----------------
Docker deployment
-----------------


.. code-block:: bash

    docker build -t mockerena .
    docker run -it -p 5000:5000 mockerena

    # Or using docker compose
    docker-compose up -d

----------------
Local deployment
----------------

To run a serverless setup locally, run:

.. code-block:: bash

    sls wsgi serve

Navigate to `localhost:5000 <http://localhost:5000>`_ to see your app running locally.


Or you can deploy manually running this command in your ``init.d`` or ``systemctl`` scripts:

.. code-block:: bash

    gunicorn3 --config gunicorn_config.py mockerena.app:app

-------------
Configuration
-------------

To configure Mockerena, inside ``settings.py`` there are a few settings:

.. code-block:: python

    HOST = os.environ.get('MOCKERENA_HOST', 'localhost')
    PORT = os.environ.get('MOCKERENA_PORT', 9000)
    BASE_PATH = os.environ.get('MOCKERENA_BASE_PATH', '')
    DEBUG = os.environ.get('MOCKERENA_DEBUG', False)
    SECRET_KEY = os.environ.get('MOCKERENA_SECRET_KEY', None)
    ENV = os.environ.get('MOCKERENA_ENV', 'development')


At a minimum at least update ``MOCKERENA_HOST`` and ``MOCKERENA_PORT`` to whatever the new host and port will be
and ``MOCKERENA_SECRET_KEY`` to a random hash.


There are also settings for configuring Mongo with mockerena. Update these as necessary:

.. code-block:: python

    # Database settings
    MONGO_HOST = os.environ.get('MOCKERENA_MONGO_HOST', 'localhost')
    MONGO_PORT = os.environ.get('MOCKERENA_MONGO_PORT', 27017)
    MONGO_DBNAME = os.environ.get('MOCKERENA_MONGO_DBNAME', 'mockerena')
    MONGO_AUTH_SOURCE = os.environ.get('MOCKERENA_MONGO_AUTH_SOURCE', 'mockerena')
    MONGO_USERNAME = os.environ.get('MOCKERENA_MONGO_USERNAME', '')
    MONGO_PASSWORD = os.environ.get('MOCKERENA_MONGO_PASSWORD', '')

For more configuration options visit `Eve's documentation <https://docs.python-eve.org/en/stable/config.html#global-configuration>`_