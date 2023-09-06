"""
Solution 6: What is the longest word that can be made without 
the letters in “AEIOSHRTN” (in other words, without the most common 
letters)? Make sure your solution can handle ties.


"""
import time
import logging
from pathlib import Path


# Logging for standard output
logging.basicConfig(level=logging.INFO)
logger: logging.RootLogger = logging.getLogger()

# Log results to results.log file
results_file_handler: logging.FileHandler = logging.FileHandler(
    "More_Wordplay/solutions/get-longest-non-aeioshrtn-results.log", mode="w"
)
results_file_handler.setLevel(logging.INFO)
logger.addHandler(results_file_handler)


ROOT: Path = Path("More_Wordplay")
SCRABBLE_PATH: Path = ROOT / "tests" / "fixtures" / "sowpods.txt"


# Assumption 1: dataset is sorted

# Assumption 2: All letters in dataset are uppercased (homogenous)

# Note: potentially handling Null results

# Note: handle ties (word or words)


def load_data_from_file_into_dict(file_path: str) -> dict[set[str]]:
    # Load this dataset into memory as dict[set[str]]

    # Make sure the file exists and handle errors
    data: dict[set[str]] = {}
    with open(file_path, mode="r") as f:
        for line in f:
            token: str = line.strip()
            data[token] = set(token)

    return data


def get_longest_non_aeioshrtn(scrabble_words: dict[set[str]]) -> list[str]:
    # Define a set of my invalid_letters
    INVALID_LETTERS: set[str] = {"A", "E", "I", "O", "S", "H", "R", "T", "N"}

    # Define storage for my matches list[str]
    matches: list[str] = []

    # Initialize longest_length = 0
    longest_length: int = 0

    # Loop over every word in scrabble_words
    for word_key in scrabble_words:
        # Initialize the word as valid
        valid_word: bool = True
        # for letter in word:
        for letter in scrabble_words[word_key]:
            # if letter in INVALID_LETTERS:
            if letter in INVALID_LETTERS:
                # Mark this word as invalid
                valid_word: bool = False
                # break
                break
        if not valid_word:
            continue

        # measure the length of this word
        curr_length: int = len(word_key)

        # elif curr_length > longest_legnth
        if curr_length > longest_length:
            # Update my matches as new list [current word]
            matches: list[str] = [word_key]
            longest_length: int = curr_length

        # if curr_legnth == longest_legnth
        elif curr_length == longest_length:
            # append it to my matches list
            matches.append(word_key)

    # Return my matches
    return matches


def get_longest_non_aeioshrtn_with_builtin(scrabble_words: dict[set[str]]) -> list[str]:
    # Define a set of my invalid_letters
    INVALID_LETTERS: set[str] = {"A", "E", "I", "O", "S", "H", "R", "T", "N"}

    # Define storage for my matches list[str]
    matches: list[str] = []

    # Initialize longest_length = 0
    longest_length: int = 0

    # Loop over every word in scrabble_words
    for word_key in scrabble_words:
        # If this word contains none of the INVALID_LETTERS
        if scrabble_words[word_key].isdisjoint(INVALID_LETTERS):
            # measure the length of this word
            curr_length: int = len(word_key)

            # If it is longer than the longest length
            if curr_length > longest_length:
                # Update my matches as new list [current word]
                matches: list[str] = [word_key]
                longest_length: int = curr_length

            # If its length is == longest_length
            elif curr_length == longest_length:
                # append it to my matches list
                matches.append(word_key)

    # Return my matches
    return matches


def main() -> None:
    scrabble_words: dict[set[str]] = load_data_from_file_into_dict(SCRABBLE_PATH)

    # My implementation
    first_start_time: float = time.time()
    results_my_impl: list[str] = get_longest_non_aeioshrtn(scrabble_words)
    first_end_time: float = time.time() - first_start_time

    # Builtin implementation (set.isdisjoint())
    second_start_time: float = time.time()
    results_builtin: list[str] = get_longest_non_aeioshrtn_with_builtin(scrabble_words)
    second_end_time: float = time.time() - second_start_time

    if results_my_impl == results_builtin:
        logger.info(f"{'#'*8} ✨ get-longest-non-aeioshrtn.py results ✨ {'#'*8}\n")
        logger.info(f"Results: {results_my_impl}\n")
        logger.info(f"\nTime for MY implementation: {first_end_time} seconds")
        logger.info(f"\nTime for BUILTIN implementation: {second_end_time} seconds")


if __name__ == "__main__":
    main()
