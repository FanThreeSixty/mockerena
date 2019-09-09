===========
Development
===========

------------------------
Generating documentation
------------------------

You can either use makefile:

.. code-block:: bash

    cd docs
    make html

Or you can use autobuild:

.. code-block:: bash

    cd docs
    sphinx-autobuild . _build/html/

Or you can use the script:

.. code-block:: bash

    script/docs


---------------
Linting project
---------------

You can run pylint yourself:

.. code-block:: bash

    pylint mockerena

Or you can use the script:

.. code-block:: bash

    script/lint


-------------
Running tests
-------------

Testing requires 3 python libraries to be installed prior to running. If you use the ``test`` script you can avoid installing these dependencies yourself.
To install dependencies run:

.. code-block:: bash

    pip install pytest pytest-cov pytest-flask

Once the dependencies are installed you can run pytest yourself:

.. code-block:: bash

    pytest

Or you can use the script:

.. code-block:: bash

    script/test


---------------------
Updating dependencies
---------------------

You can run pip update yourself:

.. code-block:: bash

    pip install -U -r requirements.txt

Or you can use the script:

.. code-block:: bash

    script/update