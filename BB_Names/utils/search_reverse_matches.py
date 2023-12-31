from collections.abc import Iterable
import time
import logging

logging.basicConfig(level=logging.INFO)
logger: logging.RootLogger = logging.getLogger()


def search_reverse_matches(
    scrabble_words: Iterable[str], baby_names: Iterable[str]
) -> float:
    """
    This function searches through two collections of strings, determines whether any
    strings in the first collection when reversed are present in the second collection,
    and prints the matches as well as time taken for the search to standard output.
    """

    # Empty set to hold our answers
    matches: set[str] = set()

    # TIME THIS
    t = time.time()

    # Loop over each baby name
    for name in baby_names:
        # Reverse that name
        reversed_name: str = name[::-1].upper()
        # Check if that reversed name is in scrabble words
        if reversed_name in scrabble_words:
            # If it is, add it to our matches set
            matches.add(name)

    # END TIME
    end_time = time.time()
    total_time = end_time - t
    # Return our correct ansers as a set
    logger.debug(matches)
    logger.debug(f"Total time taken: {total_time}\n")

    # Return matches and total_time as a tuple
    return total_time
