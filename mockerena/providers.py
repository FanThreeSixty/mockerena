"""Provider types not covered by vanilla Faker

.. codeauthor:: John Lane <john.lane93@gmail.com>

"""

import random
from typing import Any
from faker.providers import BaseProvider
import exrex


class MockProvider(BaseProvider):
    """Provider instance for types not supported by Faker
    """

    # noinspection PyMethodMayBeStatic
    def empty(self) -> str:  # pylint: disable=R0201
        """Returns an empty response

        :return:
        """

        return ''

    # noinspection PyMethodMayBeStatic
    def regex(self, expression: str = '') -> str:  # pylint: disable=R0201
        """Returns a string generated from a regular expression

        :param str expression: Regular expression
        :return:
        """

        return exrex.getone(expression if isinstance(expression, str) else '')

    # noinspection PyMethodMayBeStatic
    def price(self, minimum: int = 0, maximum: int = 999999) -> float:  # pylint: disable=R0201
        """Returns a random price within the range provided

        :param int minimum: Minimum price
        :param int maximum: Maximum price
        :return: Random price within range
        :rtype: float
        """

        minimum = minimum if isinstance(minimum, int) else 0
        maximum = maximum if isinstance(maximum, int) else 999999
        return round(random.uniform(minimum, maximum), 2)

    # noinspection PyMethodMayBeStatic
    def weighted_choice(self, elements: list, weights: list = None) -> Any:  # pylint: disable=R0201
        """Returns a random element from a list of weighted choices

        :param list elements: List of choices
        :param list weights: Weights to give each choice. Must be equal length to elements
        :return:
        """

        assert all([isinstance(attr, (list, tuple)) for attr in (elements, weights)]) and len(elements) == len(weights)
        return random.choices(elements, weights=weights)[0]
