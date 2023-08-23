"""
Solution 4: What is the shortest country name? Make sure your solution can handle ties.
"""

import logging

logger: logging.RootLogger = logging.getLogger()


def get_shortest_name(data: list[str]) -> list[str]:
    """
    This function should consume the data in countries.txt and return the country(s) with
    the shortest name, handling ties if there are more than one.
    """
