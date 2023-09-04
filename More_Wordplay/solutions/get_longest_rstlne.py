"""
Solution 5: What is the longest word that can be made from only the 
letters in “RSTLNE”? Not all of those letters need to be used, and 
letters can be repeated. Make sure your solution can handle ties.
"""

from pathlib import Path

ROOT: Path = Path("More_Wordplay")
SCRABBLE_PATH: Path = ROOT / "tests" / "fixtures" / "sowpods.txt"


# Assumption 1: all words are homogenously uppercased

# Assumption 2: target letters in words can be repeated


def runner(test: bool = False):
    scrabble_words: list[str] = load_data_from_file(SCRABBLE_PATH)
    results: list[str] = get_longest_rstlne(scrabble_words)
    return results


def load_data_from_file(file_path: str) -> list[str]:
    # load data into memory as a list[str]
    with open(SCRABBLE_PATH, mode="r") as f:
        data: list[str] = f.read().splitlines()

    return data


def update_match_list(
    length: int, match: str, longest_length: int, longest_rstlne_word: list[str]
) -> None:
    """Not implemented."""
    # If this length is greater than longest_length overwrite our list of longest
    # matches
    if length > longest_length:
        longest_rstlne_words = [match]
    # If this length is equal to the longest_length, append the word
    elif length == longest_length:
        longest_rstlne_words.append(match)


def get_longest_rstlne(scrabble_words: list[str]) -> list[str]:
    # define target letters as a set[str]
    VALID_LETTERS: set[str] = {"R", "S", "T", "L", "N", "E"}

    # initialize longest_length variable = 0
    longest_length: int = 0
    # longest_rstlne_word = []
    longest_rstlne_words: list[str] = []

    # Loop over every word in scrabble_words
    for word in scrabble_words:
        # if set(word) is a subset of target letters
        if set(word).issubset(VALID_LETTERS):
            # measure its length
            curr_length: int = len(word)

            # If this length is greater than longest_length overwrite our list of
            # longest matches
            if curr_length > longest_length:
                longest_rstlne_words = [word]
                # Update the longest_length
                longest_length: int = curr_length
            # If this length is equal to the longest_length, append the word
            elif curr_length == longest_length:
                longest_rstlne_words.append(word)

    # Return longest_matches
    return longest_rstlne_words


if __name__ == "__main__":
    print(runner())
