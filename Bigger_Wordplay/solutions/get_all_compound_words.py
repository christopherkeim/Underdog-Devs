"""
Solution 5: What are all of the compound words? These are words made 
up of 2 smaller words. For example, “SNOWMAN” is a compound word made 
from “SNOW” and “MAN”, and “BEACHBALL” is a compound word made from 
“BEACH” and “BALL”.
"""

# Q1: Are "compound words" constructed from individual words in sowpods.txt?


# Create full set of all possible permutations of sowpods (len 2 -> AA + AAH, AAH + AA)

# Loop through dataset and check for membership against ^


# Rolling hash -> look this up

from typing import Set
from pathlib import Path


SCRABBLE_PATH: Path = Path("Bigger_Wordplay/tests/fixtures/sowpods.txt")


def get_all_compound_words(path: Path) -> Set[str]:
    matches: Set[str] = set()

    # Loop over each word in the dataset file
    with open(path, mode="r") as f:
        data: Set[str] = set(f.read().splitlines())

    # Loop over each word word in the dataset
    for word in data:
        # Pointer for sliding substring window
        pointer: int = 1
        # Iterate until pointer reaches end of given word
        while pointer < len(word):
            # Slice to discover first word if it exists
            curr_compound: str = word[0:pointer]
            if curr_compound in data:
                # Slice to discover second word
                second_compound: str = word[pointer:]
                if second_compound in data:
                    matches.add(word)
                    # Move to next word (matches tend to be compound
                    # in multiple ways)
                    break
            pointer += 1

    return matches


if __name__ == "__main__":
    matches: Set[str] = get_all_compound_words(SCRABBLE_PATH)
    for word in matches:
        print(word)
