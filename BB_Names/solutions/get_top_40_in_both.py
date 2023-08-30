"""
Solution 4: What are all of the names that were top 40 baby names in both 1880 and 2020?

Note: Constant time lookup for searching hash maps

Assumption 1: All of the text in the file is single line names that are valid
unicode strings

Assumption 2: Datasets are unsorted
"""


import logging
from BB_Names.utils.load_data import load_set

# Logging for standard output
logging.basicConfig(level=logging.INFO)
logger: logging.RootLogger = logging.getLogger()

DATA_2020: str = "BB_Names/tests/fixtures/baby_names_2020_short.txt"
DATA_1880: str = "BB_Names/tests/fixtures/baby_names_1880_short.txt"


def get_top_40_in_both() -> set[str]:
    """
    This function should consume the data in two lists of names, find the union
    between both of those datasets, and return them as a set of names.
    """

    # load baby_names_2020_short.txt into a set[str]
    baby_names_2020: set[str] = load_set(DATA_2020)

    # load baby_names_1880_short.txt into a set[str]
    baby_names_1880: set[str] = load_set(DATA_1880)

    # Initalize an empty matches set
    matches: set[str] = set()

    # Loop over each name in baby_names_2020
    for name_2020 in baby_names_2020:
        # If this name is in baby_names_1880 add it to our matches set
        if name_2020 in baby_names_1880:
            matches.add(name_2020)

    # Return our matches
    return matches


# Main
if __name__ == "__main__":
    result: set[str] = get_top_40_in_both()
    logger.info(
        "Matches in baby_names_2020_short.txt and baby_names_1880_short.txt: \n"
    )
    logger.info(result)
