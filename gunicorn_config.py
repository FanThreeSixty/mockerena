"""gunicorn_config.py

.. codeauthor:: Michael Holtzscher <mholtzscher@fanthreesixty.com>

"""

bind = "0.0.0.0:5000"  # pylint: disable=C0103
workers = 2  # pylint: disable=C0103
