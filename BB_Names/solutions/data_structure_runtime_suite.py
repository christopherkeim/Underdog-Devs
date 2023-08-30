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
import time
import numpy as np
import pandas as pd
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


# Logging for standard output
logging.basicConfig(level=logging.INFO)
logger: logging.RootLogger = logging.getLogger()

# Log results to results.log file
results_file_handler: logging.FileHandler = logging.FileHandler(
    "BB_Names/solutions/results.log", mode="w"
)
results_file_handler.setLevel(logging.INFO)
logger.addHandler(results_file_handler)

# Paths to datasets
BABY_PATH: str = "BB_Names/tests/fixtures/baby_names_2020_short.txt"
SCRABBLE_PATH: str = "BB_Names/tests/fixtures/sowpods.txt"


def get_backwards_valid_scrabble_with_tuple() -> float:
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
    logger.debug("Measuring TUPLE")
    runtime: float = search_reverse_matches(scrabble_words, baby_names)
    return runtime


def get_backwards_valid_scrabble_with_list() -> float:
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
    logger.debug("Measuring LIST")
    runtime: float = search_reverse_matches(scrabble_words, baby_names)
    return runtime


def get_backwards_valid_scrabble_with_dict() -> float:
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
    logger.debug("Measuring DICT")
    runtime: float = search_reverse_matches(scrabble_words, baby_names)
    return runtime


def get_backwards_valid_scrabble_with_set() -> float:
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
    logger.debug("Measuring SET")
    runtime: float = search_reverse_matches(scrabble_words, baby_names)
    return runtime


def get_backwards_valid_scrabble_with_frozenset() -> float:
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
    logger.debug("Measuring FROZENSET")
    runtime: float = search_reverse_matches(scrabble_words, baby_names)
    return runtime


def get_backwards_valid_scrabble_with_deque() -> float:
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
    logger.debug("Measuring DEQUE")
    runtime: float = search_reverse_matches(scrabble_words, baby_names)
    return runtime


def get_backwards_valid_scrabble_with_numpy_array() -> float:
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
    logger.debug("Measuring NP.NDARRAY")
    runtime: float = search_reverse_matches(scrabble_words, baby_names)
    return runtime


def runtime_tester(iters: int = 100) -> tuple[float, pd.DataFrame]:
    """
    This function tests the runtimes of different data structures a given
    number of times, calculates their average runtimes, and returns the
    results in a pandas DataFrame.
    """
    # Define our indices for pd.DataFrame
    indices: list[str] = [
        "Tuple",
        "List",
        "Dict",
        "Set",
        "Frozen Set",
        "Deque",
        "np.ndarray",
    ]

    # Define our columns for pd.DataFrame
    cols = ["avg_runtimes_seconds"]

    # Initialize a dictionary to hold our measured runtimes
    runtime_dict: dict[str, float] = dict.fromkeys(indices, 0.0)

    # START TIME TEST
    start_time_test: float = time.time()

    # For a total of iters
    for i in range(iters):
        # Progress
        if i % 100 == 0:
            logger.info(
                f"Iteration: {i}/{iters} at {time.time() - start_time_test} seconds."
            )
        if i + 1 == iters:
            logger.info(
                f"Iteration: {i}/{iters} at {time.time() - start_time_test} seconds"
            )
        # Measure our runtimes
        time_tuple: float = get_backwards_valid_scrabble_with_tuple()
        time_list: float = get_backwards_valid_scrabble_with_list()
        time_dict: float = get_backwards_valid_scrabble_with_dict()
        time_set: float = get_backwards_valid_scrabble_with_set()
        time_frozen_set: float = get_backwards_valid_scrabble_with_frozenset()
        time_deque: float = get_backwards_valid_scrabble_with_deque()
        time_numpy_array: float = get_backwards_valid_scrabble_with_numpy_array()

        # Collect our runtimes
        runtimes: list[float] = [
            time_tuple,
            time_list,
            time_dict,
            time_set,
            time_frozen_set,
            time_deque,
            time_numpy_array,
        ]

        # Add these values to to the dictionary
        for ind, key in enumerate(runtime_dict):
            runtime_dict[key] += runtimes[ind]

    # END TIME TEST
    end_time_test: float = time.time()
    total_time_test: float = end_time_test - start_time_test

    # Calculate our average runtimes
    avg_runtimes: list[float] = [(rt / iters) for rt in list(runtime_dict.values())]

    # Construct our DataFrame
    avg_runtime_df: pd.DataFrame = pd.DataFrame(
        avg_runtimes, index=indices, columns=cols
    )

    # Return our average calculated runtimes as a pd.DataFrame
    return (total_time_test, avg_runtime_df)


# Main
if __name__ == "__main__":
    # Calculate the average runtimes for a desired number of test iterations
    iterations: int = 100
    logger.info(f"Calculating average runtimes for {iterations} iterations 🚀.\n")

    total_time_test, avg_runtime_df = runtime_tester(iters=iterations)

    # Log our results
    logger.info(f"\n{'#'*9} ✨ Data Structure Runtime Suite Results ✨ {'#'*9}\n")
    logger.info(f"\n{avg_runtime_df.sort_values(by='avg_runtimes_seconds')}\n")
    logger.info(f"Completed in: {total_time_test} seconds 😳.")
