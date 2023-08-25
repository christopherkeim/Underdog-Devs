"""
Solution 1: What is the shortest baby name in the top 40 baby names for 2020?
"""

import logging

logger: logging.RootLogger = logging.getLogger()


def get_shortest_in_top_40(data: list[str]) -> str:
    """
    This function should consume the data in baby_names_2020_short.txt and
    return the shortest baby name in this dataset.

    Note that this can be discovered using one loop visiting each of the memory
    locations in this list, and thus operates in O(n) runtime complexity.

    However, handling ties in this dataset would require O(n^2) runtime complexity,
    as we would first have to discover the shortest length by visiting each memory
    location in the list and then iterate through it again filtering for that
    length condition.
    """

    # Check that we have the correct parameter input data type
    if not isinstance(data, list) or not all(isinstance(name, str) for name in data):
        raise TypeError("This function requires a list of strings as input.")

    # Initialize the shortest_name variable
    shortest_name: str = None

    # Initialize the shortest_length variable
    shortest_length: int = 30

    # Loop over each word in our dataset and discover the shortest length
    logger.info("Discovering the shortest name.")
    for name in data:
        # If the length of this name is smaller than shorter length
        if len(name) < shortest_length:
            # Update shortest_length and shortest_name
            shortest_length = len(name)
            shortest_name = name

    # Return the shortest name
    return shortest_name
