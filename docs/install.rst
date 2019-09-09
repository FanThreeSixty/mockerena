===============
Getting Started
===============

Install through git:

.. code-block:: bash

    git clone https://github.com/FanThreeSixty/mockerena


Either you can install the project yourself or you can use the prepared scripts

To use the prepared scripts use:

.. code-block:: bash

    cd mockerena
    script/setup

To install dependencies yourself:

.. code-block:: bash

    cd mockerena
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt
    pip install -e .

To run the project either use:

.. code-block:: bash

    script/server

Or manually through:

.. code-block:: bash

    python mockerena/app.py