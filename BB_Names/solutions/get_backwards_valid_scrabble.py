"""
Solution 3: There is at least one baby name from the top 40 baby names
for 2020 that, when spelled backwards, is a valid Scrabble word. Find and 
print all such names.

Solve this two ways: first with an array to hold the Scrabble words, and then 
with a dictionary (or set) to hold the Scrabble words. Use timer functions to 
measure how long it takes to complete this work under each implementation. 
Why is the time different?
"""
import time
import logging

logging.basicConfig(level=logging.INFO)
logger: logging.RootLogger = logging.getLogger()

"""
Implementation 1: scrabble words as a list[str]
"""


def get_backwards_valid_scrabble_with_2_lists() -> None:
    """ """
    # Load scrabble words into a data structure - list[str]
    with open("BB_Names/tests/fixtures/sowpods.txt", mode="r") as sw:
        scrabble_words = sw.read().splitlines()
    # Load baby names into a data structure - list[str]
    with open("BB_Names/tests/fixtures/baby_names_2020_short.txt", mode="r") as bn:
        baby_names = bn.read().splitlines()
    # Empty set to hold our answers
    matches: set[str] = set()

    # Validate data type is correct

    # Validate that values are correct (not "" or other objects)

    # TIME THIS
    logger.info("Using get_backwards_valid_scrabble_with_2_lists()")
    t = time.time()
    # Loop over each baby name
    for name in baby_names:
        # reverse that name
        current_name: str = name[::-1].upper()
        # check if that reversed name is in scrabble words
        if current_name in scrabble_words:
            # if it is, add it to our correct_answers set
            matches.add(name)

    # END TIME
    end_time = time.time()
    total_time = end_time - t
    # Return our correct ansers as a set
    logger.info(matches)
    logger.info(f"Total time taken: {total_time}\n")


"""
Implementation 2: scrabble words as a set
"""


def get_backwards_valid_scrabble_with_bn_list_sw_set() -> None:
    """ """
    # Load scrabble words into a data structure - list[str]
    with open("BB_Names/tests/fixtures/sowpods.txt", mode="r") as sw:
        scrabble_words: set[str] = set(sw.read().splitlines())
    # Load baby names into a data structure - list[str]
    with open("BB_Names/tests/fixtures/baby_names_2020_short.txt", mode="r") as bn:
        baby_names: list[str] = bn.read().splitlines()
    # Empty set to hold our answers
    matches: set[str] = set()

    # TIME THIS
    logger.info("Using get_backwards_valid_scrabble_with_bn_list_sw_set()")
    t = time.time()
    # Loop over each baby name
    for name in baby_names:
        # reverse that name
        current_name: str = name[::-1].upper()
        # check if that reversed name is in scrabble words
        if current_name in scrabble_words:
            # if it is, add it to our correct_answers set
            matches.add(name)

    # END TIME
    end_time = time.time()
    total_time = end_time - t
    # Return our correct ansers as a set
    logger.info(matches)
    logger.info(f"Total time taken: {total_time}\n")


"""
Implementation 3: both as sets
"""


def get_backwards_valid_scrabble_with_both_sets() -> None:
    """ """

    # Load the scrabble words and baby names datasets as sets
    scrabble_words, baby_names = load_data(sn_set=True, bn_set=True)

    # Empty set to hold our answers
    matches: set[str] = set()

    # TIME THIS
    logger.info("Using get_backwards_valid_scrabble_with_both_sets()")
    t = time.time()
    # Loop over each baby name
    for name in baby_names:
        # reverse that name
        current_name: str = name[::-1].upper()
        # check if that reversed name is in scrabble words
        if current_name in scrabble_words:
            # if it is, add it to our correct_answers set
            matches.add(name)

    # END TIME
    end_time = time.time()
    total_time = end_time - t
    # Return our correct ansers as a set
    logger.info(matches)
    logger.info(f"Total time taken: {total_time}\n")


"""
Implementation 4: baby names as a set, scrabble words as a list
"""


def get_backwards_valid_scrabble_with_sw_list_bn_set() -> None:
    """ """
    # Load scrabble words into a data structure - list[str]
    with open("BB_Names/tests/fixtures/sowpods.txt", mode="r") as sw:
        scrabble_words: list[str] = sw.read().splitlines()
    # Load baby names into a data structure - set[str]
    with open("BB_Names/tests/fixtures/baby_names_2020_short.txt", mode="r") as bn:
        baby_names: set[str] = set(bn.read().splitlines())

    # Empty set to hold our answers
    matches: set[str] = set()

    # TIME THIS
    logger.info("Using get_backwards_valid_scrabble_with_sw_list_bn_set()")
    t = time.time()
    # Loop over each baby name
    for name in baby_names:
        # reverse that name
        current_name: str = name[::-1].upper()
        # check if that reversed name is in scrabble words
        if current_name in scrabble_words:
            # if it is, add it to our correct_answers set
            matches.add(name)

    # END TIME
    end_time = time.time()
    total_time = end_time - t
    # Return our correct ansers as a set
    logger.info(matches)
    logger.info(f"Total time taken: {total_time}\n")


"""
Comparison function
"""


def extract_matches() -> None:
    """
    This function searches through two collections of strings, determines whether any
    strings in the first collection when reversed are present in the second collection,
    and prints the matches as well as time taken for the search to standard output.
    """
    # TIME THIS
    t = time.time()
    # Loop over each baby name
    for name in baby_names:
        # reverse that name
        current_name: str = name[::-1].upper()
        # check if that reversed name is in scrabble words
        if current_name in scrabble_words:
            # if it is, add it to our correct_answers set
            matches.add(name)

    # END TIME
    end_time = time.time()
    total_time = end_time - t
    # Return our correct ansers as a set
    logger.info(matches)
    logger.info(f"Total time taken: {total_time}\n")


if __name__ == "__main__":
    get_backwards_valid_scrabble_with_2_lists()
    get_backwards_valid_scrabble_with_bn_list_sw_set()
    get_backwards_valid_scrabble_with_both_sets()
    get_backwards_valid_scrabble_with_sw_list_bn_set()
