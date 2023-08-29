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

    # Check that we have the correct parameter input value
    if not all(len(name) > 0 for name in data):
        raise ValueError(
            "This function requires a list of strings greater than length 0."
        )

    # Initialize a list[str] for longest_names
    longest_names: list[str] = []

    # Initialize a length counter
    longest_length: int = 0

    # Loop through each name in our list to discover longest name in list
    logger.info("Discovering the longest names in our dataset.")
    for name in data:
        if len(name) > longest_length:
            longest_length = len(name)

    # Loop through each name in the list and extract the names matching
    # our discovered longest length
    logger.info("Extracting the longest names from our dataset.")
    for name in data:
        if len(name) == longest_length:
            longest_names.append(name)

    # Return the longest names
    return longest_names
