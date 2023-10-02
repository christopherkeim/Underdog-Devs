"""
Solution 4: Write a function that takes a string availableLetters 
as an argument and returns an array of all of the words that can 
be made from only those letters. Letters can be re-used as many times 
as needed and can appear in any order. 

Not all of the letters in availableLetters have to be used.
"""

# Note: the dataset is presorted

# Note: all letters are homogenously cased


from typing import List, Set
from pathlib import Path


def get_words_from_available_letters(available_letters: str) -> List[str]:
    SCRABBLE_PATH: Path = Path("Bigger_Wordplay/tests/fixtures/sowpods.txt")

    # Cast available letters as a set
    AVAILABLE_LETTERS: Set[str] = set(available_letters)

    # Initialize matches list
    matches: List[str] = []

    # Loop over each word in the dataset file
    with open(SCRABBLE_PATH, mode="r") as f:
        for word in f:
            # Strip out \n
            word: str = word.strip()

            if len(set(word).difference(AVAILABLE_LETTERS)) == 0:
                matches.append(word)

    return matches


if __name__ == "__main__":
    print(get_words_from_available_letters("ABCDE"))
