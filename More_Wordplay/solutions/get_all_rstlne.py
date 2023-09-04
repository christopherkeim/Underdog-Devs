"""
Solution 4: What are all of the words that can be made from only the letters 
in “RSTLNE”? Not all of those letters need to be used, and letters can be repeated.


Note: you are decomposing a word into its unique elements 

HOMEWORK:  Read your data as a list[set[str]] 
"""

# Assumptions 1: the dataset is finite and can be 0 words

# Assumption 2: all letters are homogenous

# Assumption 3: there are repeated letters in each word

from pathlib import Path

ROOT: Path = Path("More_Wordplay")

SCRABBLE_WORDS: Path = ROOT / "tests" / "fixtures" / "sowpods.txt"


def runner(test: bool = False) -> None:
    scrabble_words: list[str] = load_data_from_file(SCRABBLE_WORDS)
    results: list[str] = get_all_rstlne(scrabble_words)

    return results


def load_data_from_file(file_path: str) -> list[str]:
    """
    Takes a file path as input, reads that file into memory, and
    returns that file as a list of strings.
    """
    with open(file_path, mode="r") as f:
        data: list[str] = f.read().splitlines()

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


if __name__ == "__main__":
    print(runner())
