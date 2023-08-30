"""
Solution 3: There is at least one baby name from the top 40 baby names
for 2020 that, when spelled backwards, is a valid Scrabble word. Find and 
print all such names.

Solve this two ways: first with an array to hold the Scrabble words, and then 
with a dictionary (or set) to hold the Scrabble words. Use timer functions to 
measure how long it takes to complete this work under each implementation. 
Why is the time different?
"""

import logging
from BB_Names.utils.load_data import load_list, load_set
from BB_Names.utils.search_reverse_matches import search_reverse_matches

logging.basicConfig(level=logging.INFO)
logger: logging.RootLogger = logging.getLogger()

BABY_PATH: str = "BB_Names/tests/fixtures/baby_names_2020_short.txt"
SCRABBLE_PATH: str = "BB_Names/tests/fixtures/sowpods.txt"


"""
Implementation 1: both as a list[str]
"""


def get_backwards_valid_scrabble_with_2_lists() -> None:
    """
    This function searches for baby names from the baby_names_2020_short.txt
    dataset thatwhen spelled backwards are a valid Scrabble words in the
    sowpods.txt dataset.

    The DATA STRUCTURES used here are:

    SCRABBLE_WORDS: list[str]
    BABY_NAMES: list[str]
    """
    # Load scrabble words into a data structure - list[str]
    scrabble_words: list[str] = load_list(SCRABBLE_PATH)
    # Load baby names into a data structure - list[str]
    baby_names: list[str] = load_list(BABY_PATH)

    # Validate data type is correct

    # Validate that values are correct (not "" or other objects)

    # Search for reverse matches
    logger.info("Using get_backwards_valid_scrabble_with_2_lists()")
    search_reverse_matches(scrabble_words, baby_names)


"""
Implementation 2: scrabble words as a set[str] baby names as list[str]
"""


def get_backwards_valid_scrabble_with_bn_list_sw_set() -> None:
    """
    This function searches for baby names from the baby_names_2020_short.txt
    dataset thatwhen spelled backwards are a valid Scrabble words in the
    sowpods.txt dataset.

    The DATA STRUCTURES used here are:

    SCRABBLE_WORDS: set[str]
    BABY_NAMES: list[str]
    """
    # Load scrabble words into a data structure - list[str]
    scrabble_words: set[str] = load_set(SCRABBLE_PATH)
    # Load baby names into a data structure - list[str]
    baby_names: list[str] = load_list(BABY_PATH)

    # Search for reverse matches
    logger.info("Using get_backwards_valid_scrabble_with_bn_list_sw_set()")
    search_reverse_matches(scrabble_words, baby_names)


"""
Implementation 3: both as set[str]
"""


def get_backwards_valid_scrabble_with_both_sets() -> None:
    """
    This function searches for baby names from the baby_names_2020_short.txt
    dataset thatwhen spelled backwards are a valid Scrabble words in the
    sowpods.txt dataset.

    The DATA STRUCTURES used here are:

    SCRABBLE_WORDS: set[str]
    BABY_NAMES: set[str]
    """
    # Load scrabble words into a data structure - list[str]
    scrabble_words: set[str] = load_set(SCRABBLE_PATH)
    # Load baby names into a data structure - list[str]
    baby_names: set[str] = load_set(BABY_PATH)

    # Search for reverse matches
    logger.info("Using get_backwards_valid_scrabble_with_both_sets()")
    search_reverse_matches(scrabble_words, baby_names)


"""
Implementation 4: baby names as a set[str], scrabble words as a list[str]
"""


def get_backwards_valid_scrabble_with_sw_list_bn_set() -> None:
    """
    This function searches for baby names from the baby_names_2020_short.txt
    dataset thatwhen spelled backwards are a valid Scrabble words in the
    sowpods.txt dataset.

    The DATA STRUCTURES used here are:

    SCRABBLE_WORDS: list[str]
    BABY_NAMES: set[str]
    """

    # Load scrabble words into a data structure - list[str]
    scrabble_words: list[str] = load_list(SCRABBLE_PATH)

    # Load baby names into a data structure - set[str]
    baby_names: set[str] = load_set(BABY_PATH)

    # Search for reverse matches
    logger.info("Using get_backwards_valid_scrabble_with_sw_list_bn_set()")
    search_reverse_matches(scrabble_words, baby_names)


if __name__ == "__main__":
    get_backwards_valid_scrabble_with_2_lists()
    get_backwards_valid_scrabble_with_bn_list_sw_set()
    get_backwards_valid_scrabble_with_both_sets()
    get_backwards_valid_scrabble_with_sw_list_bn_set()
