"""
This script tests the runtimes of different data structures in Python using two 
datasets: the baby_names_2020_short.txt dataset and the sowpods.txt dataset.

For all tests, the baby_names_2020_short.txt dataset will be loaded into 
memory as a list[str] and this data structure will be held CONSTANT across tests.

THE DATA STRUCTURE USED TO HOLD THE SOWPODS.TXT FILE WILL BE VARIED.

The code to implement our search algorithm in search_reverse_matches() will be
held CONSTANT as well - we are measuring how this search algorithm's runtime
varies as a function of the data structure it is searching through.

The Data Structures measured here are (sowpods.txt):

- tuple
- list
- dict
- set
- frozenset
- deque
- np.ndarray

"""

from collections import deque
import numpy as np
import logging
from BB_Names.utils.load_data import (
    load_tuple,
    load_list,
    load_dict,
    load_set,
    load_frozen_set,
    load_deque,
    load_numpy_array,
)
from BB_Names.utils.search_reverse_matches import search_reverse_matches

logging.basicConfig(level=logging.INFO)
logger: logging.RootLogger = logging.getLogger()

BABY_PATH: str = "BB_Names/tests/fixtures/baby_names_2020_short.txt"
SCRABBLE_PATH: str = "BB_Names/tests/fixtures/sowpods.txt"


def get_backwards_valid_scrabble_with_tuple() -> None:
    """
    This function searches for baby names from the baby_names_2020_short.txt
    dataset thatwhen spelled backwards are a valid Scrabble words in the
    sowpods.txt dataset.

    The DATA STRUCTURES used here are:

    SCRABBLE_WORDS: tuple[str]
    BABY_NAMES: list[str]
    """
    # Load scrabble words into a data structure - tuple[str]
    scrabble_words: tuple[str] = load_tuple(SCRABBLE_PATH)
    # Load baby names into a data structure - list[str]
    baby_names: list[str] = load_list(BABY_PATH)

    # Search for reverse matches
    logger.info("Measuring TUPLE")
    search_reverse_matches(scrabble_words, baby_names)


def get_backwards_valid_scrabble_with_list() -> None:
    """
    This function searches for baby names from the baby_names_2020_short.txt
    dataset thatwhen spelled backwards are a valid Scrabble words in the
    sowpods.txt dataset.

    The DATA STRUCTURES used here are:

    SCRABBLE_WORDS: list[str]
    BABY_NAMES: list[str]
    """
    # Load scrabble words into a data structure - tuple[str]
    scrabble_words: list[str] = load_list(SCRABBLE_PATH)
    # Load baby names into a data structure - list[str]
    baby_names: list[str] = load_list(BABY_PATH)

    # Search for reverse matches
    logger.info("Measuring LIST")
    search_reverse_matches(scrabble_words, baby_names)


def get_backwards_valid_scrabble_with_dict() -> None:
    """
    This function searches for baby names from the baby_names_2020_short.txt
    dataset thatwhen spelled backwards are a valid Scrabble words in the
    sowpods.txt dataset.

    The DATA STRUCTURES used here are:

    SCRABBLE_WORDS: dict[str, bool]
    BABY_NAMES: list[str]
    """
    # Load scrabble words into a data structure - dict[str, bool]
    scrabble_words: dict[str, bool] = load_dict(SCRABBLE_PATH)
    # Load baby names into a data structure - list[str]
    baby_names: list[str] = load_list(BABY_PATH)

    # Search for reverse matches
    logger.info("Measuring DICT")
    search_reverse_matches(scrabble_words, baby_names)


def get_backwards_valid_scrabble_with_set() -> None:
    """
    This function searches for baby names from the baby_names_2020_short.txt
    dataset thatwhen spelled backwards are a valid Scrabble words in the
    sowpods.txt dataset.

    The DATA STRUCTURES used here are:

    SCRABBLE_WORDS: set[str]
    BABY_NAMES: list[str]
    """
    # Load scrabble words into a data structure - set[str]
    scrabble_words: set[str] = load_set(SCRABBLE_PATH)
    # Load baby names into a data structure - list[str]
    baby_names: list[str] = load_list(BABY_PATH)

    # Search for reverse matches
    logger.info("Measuring SET")
    search_reverse_matches(scrabble_words, baby_names)


def get_backwards_valid_scrabble_with_frozenset() -> None:
    """
    This function searches for baby names from the baby_names_2020_short.txt
    dataset thatwhen spelled backwards are a valid Scrabble words in the
    sowpods.txt dataset.

    The DATA STRUCTURES used here are:

    SCRABBLE_WORDS: frozenset[str]
    BABY_NAMES: list[str]
    """
    # Load scrabble words into a data structure - frozenset[str]
    scrabble_words: frozenset[str] = load_frozen_set(SCRABBLE_PATH)
    # Load baby names into a data structure - list[str]
    baby_names: list[str] = load_list(BABY_PATH)

    # Search for reverse matches
    logger.info("Measuring FROZENSET")
    search_reverse_matches(scrabble_words, baby_names)


def get_backwards_valid_scrabble_with_deque() -> None:
    """
    This function searches for baby names from the baby_names_2020_short.txt
    dataset thatwhen spelled backwards are a valid Scrabble words in the
    sowpods.txt dataset.

    The DATA STRUCTURES used here are:

    SCRABBLE_WORDS: deque[str]
    BABY_NAMES: list[str]
    """
    # Load scrabble words into a data structure - deque[str]
    scrabble_words: deque[str] = load_deque(SCRABBLE_PATH)
    # Load baby names into a data structure - list[str]
    baby_names: list[str] = load_list(BABY_PATH)

    # Search for reverse matches
    logger.info("Measuring DEQUE")
    search_reverse_matches(scrabble_words, baby_names)


def get_backwards_valid_scrabble_with_numpy_array() -> None:
    """
    This function searches for baby names from the baby_names_2020_short.txt
    dataset thatwhen spelled backwards are a valid Scrabble words in the
    sowpods.txt dataset.

    The DATA STRUCTURES used here are:

    SCRABBLE_WORDS: np.ndarray[str]
    BABY_NAMES: list[str]
    """
    # Load scrabble words into a data structure - deque[str]
    scrabble_words: np.ndarray[str] = load_numpy_array(SCRABBLE_PATH)
    # Load baby names into a data structure - list[str]
    baby_names: list[str] = load_list(BABY_PATH)

    # Search for reverse matches
    logger.info("Measuring NP.NDARRAY")
    search_reverse_matches(scrabble_words, baby_names)


# Main
if __name__ == "__main__":
    get_backwards_valid_scrabble_with_tuple()
    get_backwards_valid_scrabble_with_list()
    get_backwards_valid_scrabble_with_dict()
    get_backwards_valid_scrabble_with_set()
    get_backwards_valid_scrabble_with_frozenset()
    get_backwards_valid_scrabble_with_deque()
    get_backwards_valid_scrabble_with_numpy_array()
