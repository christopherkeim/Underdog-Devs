"""
Solution 2: What are the longest baby names in the top 40 baby names for 2020? 
Make sure you can handle if there's a tie.
"""

import logging

logger: logging.RootLogger = logging.getLogger()


def get_longest_in_top_40(data: list[str]) -> list[str]:
    """
    This function should consume the data in baby_names_2020_short.txt and
    return the longest names in this dataset, handling ties.
    """

    # Check that we have the correct parameter input data type
    if not isinstance(data, list) or not all(isinstance(name, str) for name in data):
        raise TypeError("This function requires a list of strings as input.")
