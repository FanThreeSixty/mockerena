==========
Deployment
==========

-------------
Deploy to AWS
-------------

First you'll need to install the serverless cli:

.. code-block:: bash

    npm install -g serverless


Afterwards, to deploy simply run:

.. code-block:: bash

    serverless deploy


Once the deploy is complete, run ``sls info`` to get the endpoint:

.. code-block:: bash

    sls info


----------------
Local deployment
----------------

To run a serverless setup locally, run:

.. code-block:: bash

    sls wsgi serve

Navigate to `localhost:5000 <http://localhost:5000>`_ to see your app running locally.