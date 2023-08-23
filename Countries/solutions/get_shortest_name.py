"""
Solution 4: What is the shortest country name? Make sure your solution can handle ties.
"""

import logging

logger: logging.RootLogger = logging.getLogger()


def get_shortest_name(data: list[str]) -> list[str]:
    """
    This function should consume the data in countries.txt and return the
    country(s) with the shortest name, handling ties if there are more than one.
    """

    # Check that we have the correct parameter input data type
    if not isinstance(data, list) or not all(isinstance(word, str) for word in data):
        raise TypeError("This function requires a list of strings as input.")

    # Initialize an empty list for our shortest_names
    shortest_names: list[str] = []

    # Initialize a counter for word length
    shortest_length: int = 30

    # Loop over each word in the data and discover the shortest word length
    logger.info("Sampling dataset and discovering shortest word length.")
    for word in data:
        # Measure the word's length
        curr_length: int = len(word)
        # If the current length is smaller than shortest, update shortest length
        if curr_length < shortest_length:
            shortest_length = curr_length

    # Loop over each word in the data and extract those with the shortest length
    logger.info("Extracting shortest words in dataset.")
    for word in data:
        # If the current word's length is equal to global shortest length in dataset
        if len(word) == shortest_length:
            shortest_names.append(word)

    # Return the shortest words
    return shortest_names
