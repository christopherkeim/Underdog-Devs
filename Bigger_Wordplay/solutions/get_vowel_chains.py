"""
Solution 7: Find the words in the alphabet list that contain 
the longest sequential chain of vowels.
"""
# Sequence: "AEIOU" "EIOCUA" "FEEDBACK"

# Only need the words themselves + longest length of chain

# Note: the order of vowels within the word doesn't matter
from typing import List, Tuple, Set
from pathlib import Path

SCRABBLE_WORDS: Path = Path("Bigger_Wordplay/tests/fixtures/sowpods.txt")


def get_words_made_of_longest_vowel_chain(path: Path) -> Tuple[int, List[str]]:
    # define a set of vowels
    VOWELS: Set[str] = {"A", "E", "I", "O", "U"}

    # longest_matches = []
    longest_matches: List[str] = []

    abs_longest_length: int = 0

    # Loop over each word in this dataset - one word at a time
    with open(path, mode="r") as f:
        for word in f:
            word: str = word.strip()
            working_length: int = 0
            intra_longest_length: int = 0

            # Loop over each character
            for letter in word:
                # Initialization + chain building condition
                if letter in VOWELS:
                    working_length += 1

                # Else reset the chain
                else:
                    # Update longest intra length
                    if working_length > intra_longest_length:
                        intra_longest_length = working_length
                    # Reset working legnth to 0
                    working_length = 0

            # Update longest intra length if last char is a vowel
            if working_length > intra_longest_length:
                intra_longest_length = working_length
            # Updates if intra longest is longer
            if intra_longest_length > abs_longest_length:
                abs_longest_length = intra_longest_length
                longest_matches = [word]
            # Append word to longest matches
            elif intra_longest_length == abs_longest_length:
                longest_matches.append(word)

    return abs_longest_length, longest_matches


TEST_PATH: Path = Path("Bigger_Wordplay/tests/fixtures/chain_test.txt")

if __name__ == "__main__":
    longest_len, matches = get_words_made_of_longest_vowel_chain(SCRABBLE_WORDS)
    print(f"Longest length: {longest_len}")
    print(f"Matches: {matches}")
