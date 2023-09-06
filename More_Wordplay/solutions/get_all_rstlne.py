"""
Solution 4: What are all of the words that can be made from only the letters 
in “RSTLNE”? Not all of those letters need to be used, and letters can be repeated.


Note: you are decomposing a word into its unique elements 

HOMEWORK:  Read your data as a list[set[str]] 
"""

# Assumptions 1: the dataset is finite and can be 0 words

# Assumption 2: all letters are homogenous

# Assumption 3: there are repeated letters in each word
import time
from pathlib import Path
import logging


# Logging for standard output
logging.basicConfig(level=logging.INFO)
logger: logging.RootLogger = logging.getLogger()

# Log results to results.log file
results_file_handler: logging.FileHandler = logging.FileHandler(
    "More_Wordplay/solutions/get-all-rstlne-results.log", mode="w"
)
results_file_handler.setLevel(logging.INFO)
logger.addHandler(results_file_handler)

ROOT: Path = Path("More_Wordplay")

SCRABBLE_WORDS: Path = ROOT / "tests" / "fixtures" / "sowpods.txt"


def runner(test: bool = False) -> None:
    # First implementation as list[str]
    scrabble_words1: list[str] = load_data_from_file(SCRABBLE_WORDS)

    first_start_time: float = time.time()
    results1: list[str] = get_all_rstlne(scrabble_words1)
    first_end_time: float = time.time() - first_start_time

    # Second implementation as dict[set[str]]
    scrabble_words2: dict[set[str]] = load_data_from_file_as_dict_of_sets(
        SCRABBLE_WORDS
    )

    second_start_time: float = time.time()
    results2: list[str] = get_all_rstlne_using_dict_of_sets(scrabble_words2)
    second_end_time: float = time.time() - second_start_time

    if results1 == results2:
        logger.info(f"{'#'*8} ✨ get_all_rstlne.py results ✨ {'#'*8}\n")
        for result in results1:
            logger.info(result)
        logger.info(
            f"""\n\nTime taken for first implementation (as LIST[STR]): 
            {first_end_time} seconds
            """
        )
        logger.info(
            f"""Time taken for second implementation(as DICT[SET[STR]]): 
            {second_end_time} seconds\n
            """
        )
        logger.info(f"Improvement: {(second_end_time / first_end_time) * 100}%")


def load_data_from_file(file_path: str) -> list[str]:
    """
    Takes a file path as input, reads that file into memory, and
    returns that file as a list of strings.
    """
    with open(file_path, mode="r") as f:
        data: list[str] = f.read().splitlines()

    return data


def load_data_from_file_as_dict_of_sets(file_path: str) -> dict[set[str]]:
    data: dict = {}
    with open(file_path, mode="r") as f:
        for line in f:
            token: str = line.strip()
            data[token] = set(token)
    return data


def get_all_rstlne(scrabble_words: list[str]) -> list[str]:
    # define a collection of acceptable letters 'RSTLNE' as set[str]
    RSTLNE: set[str] = {"R", "S", "T", "L", "N", "E"}

    # define storage for my matches list[str]
    matches: list[str] = []

    # Loop through each word in the dataset
    for word in scrabble_words:
        # If this word is composed of only the letters in RSTLNE
        if set(word).issubset(RSTLNE):
            # Add it to our matches
            matches.append(word)

    # Return matches
    return matches


def get_all_rstlne_using_dict_of_sets(scrabble_words: dict[set[str]]) -> list[str]:
    # Define a collection of acceptable letters as a set[str]
    RSTLNE: set[str] = {"R", "S", "T", "L", "N", "E"}

    # Define storage for matches as list[str]
    matches: list[str] = []

    # Loop through each word in the dataset
    for word_key in scrabble_words:
        # If this word is composed of only the letters in RSTLNE
        if scrabble_words[word_key].issubset(RSTLNE):
            # Add it to our matches
            matches.append(word_key)

    # Return matches
    return matches


if __name__ == "__main__":
    runner()
