"""
Solution 3: What are all of the words that have at least 3 different double letters? 
For example, “BOOKKEEPER” is an answer to this question because 
it has a double-O, a double-K, and a double-E.
"""


# Q1: is this dataset static?

# Assumption 1: a double letter occurs exactly one index in front of the
#               previous instance of that letter

# Assumption 2: all letters are homogenously cased
from typing import List, Set
from pathlib import Path


SCRABBLE_PATH: Path = Path("Bigger_Wordplay/tests/fixtures/sowpods.txt")


def get_double_letters(path: Path) -> List[str]:
    # initialize a list holding matches []
    matches: List[str] = []

    # Loop over each line (word) in the dataset
    with open(path, mode="r") as f:
        for word in f:
            # Strip out newline from word
            word: str = word.strip()
            # Initialize set to hold unique letters
            unique_double_letters: Set = set()
            # Loop over each letter
            for i in range(len(word) - 1):
                if word[i] == word[i + 1]:
                    unique_double_letters.add(word[i])

            if len(unique_double_letters) >= 3:
                matches.append(word)

    return matches


if __name__ == "__main__":
    print(get_double_letters(SCRABBLE_PATH))
