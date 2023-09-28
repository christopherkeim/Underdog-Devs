"""
Solution 2: What are all of the words that are at least 8 letters long and 
use 3 or fewer different letters? For example, “REFERRER” is an answer 
to this question, because it uses only 3 different letters: R, E, and F.
"""

"""

"""

# Note: Condition 1: word length >= 8 letters

# Note: Condition 2: only <= 3 unique letters, where frequency does not matter (set)

# Note: capitalization does not matter, but you can't assume homogenous capitalization

# Assumption 1: dataset is static


# Example 3: XXXOOORR -> positive
# Example 6: XXXXOOR -> negative
# Example 1: XXOORRTT -> negative


from typing import List, Set
from pathlib import Path


SCRABBLE_PATH: Path = Path("Bigger_Wordplay/tests/fixtures/sowpods.txt")


def get_8_letters_3_unique_or_fewer(path: Path) -> List[str]:
    matches: List[str] = []

    # Loop over each line in this datatset
    with open(path, mode="r") as f:
        for word in f:
            word: str = word.strip()
            # Measure its length
            if len(word) < 8:
                continue
            # Measure unique characters in word
            if len(set(word)) <= 3:
                matches.append(word)

    return matches


if __name__ == "__main__":
    print(get_8_letters_3_unique_or_fewer(SCRABBLE_PATH))
