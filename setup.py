#!/usr/bin/env python
"""setup.py

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

import os
from setuptools import setup
from mockerena import __author__, __email__, __license__, __version__


def read(filename):
    """Utility function to read the README file

    :param str filename: File name
    :return:
    """

    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name="mockerena",
    version=__version__,
    author=__author__,
    author_email=__email__,
    maintainer=__author__,
    maintainer_email=__email__,
    description="Self-hosting data mocking service",
    license=__license__,
    keywords="flask data mock test api",
    url="https://github.com/FanThreeSixty/mockerena",
    project_urls={
        "Home": "https://github.com/FanThreeSixty/mockerena",
        "Tracker": "https://github.com/FanThreeSixty/mockerena/issues"
    },
    packages=["mockerena"],
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    install_requires=[
        "Eve>=0.8.0",
        "exrex>=0.10.5",
        "Faker>=1.0.0",
        "flasgger>=0.9.0",
        "Flask>=1.0.0",
        "Jinja2>=2.10",
        "pandas>=0.24.0"
    ],
    python_requires=">=3.6",
    setup_requires=["pytest-runner"],
    tests_require=[
        "pytest>=4.4.0",
        "pytest-cov>=2.6.0",
        "pytest-flask>=0.14.0",
        "pytest-pep8>=1.0.0",
        "pytest-pylint>=0.14.0"
    ],
    extras_require={
        "release": [
            "bumpversion>=0.5.0",
            "Sphinx>=2.0.0",
            "sphinx-rtd-theme>=0.4.0"
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Mocking",
    ]
)
