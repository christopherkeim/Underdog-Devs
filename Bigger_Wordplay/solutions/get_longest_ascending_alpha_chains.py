"""
Solution 8: Find the words containing the longest chains of alphabetical 
(not necessarily continuous) letters. "alps" is an example of a chain 
of letters that is ascending/alphabetical.  Another example: "alphabetical" 
contains the following alphabetically ascending strings: "alp", "h", 
"abet" "i", "c", "al", so its longest ascending substring is 4 in length "abet."
"""

# Letters that match the pattern (ASCII values) l1 < l2 < l3 ... ln

# Further - longest substring matching this pattern within a given word

# Return words containing the absolute longest such chain
from typing import List, Dict
from pathlib import Path


SCRABBLE_PATH: Path = Path("Bigger_Wordplay/tests/fixtures/sowpods.txt")
TEST_PATH: Path = Path("Bigger_Wordplay/tests/fixtures/chain_test.txt")


def get_longest_ascending_alpha_chains(path: Path) -> Dict[str, str]:
    matches: Dict[str, str] = {}

    abs_longest_chain: List[str] = []

    with open(path, mode="r") as f:
        for word in f:
            word: str = word.strip()
            """
            Tracking: 
              - current pointer (letter)
              - previous pointer (letter)
              - longest chain within the word
              - globally longest chain in dataset
              - list of words that have the currently longest chain length

              --> modifications at correct times 
            
            Refactor: 
            1. Function that checks the longest chain within a word (44 - 62), 
            takes word as input and returns longest chain output 
            """

            longest_chain: List[str] = []
            working_chain: List[str] = []

            for letter in word:
                # Initialization condition and chain building condition
                if len(working_chain) == 0:
                    working_chain.append(letter)

                elif letter > working_chain[-1]:
                    working_chain.append(letter)

                else:
                    if len(working_chain) > len(longest_chain):
                        longest_chain = working_chain
                    working_chain = [letter]

            if len(working_chain) > len(longest_chain):
                longest_chain = working_chain
                working_chain = [letter]

            if len(longest_chain) > len(abs_longest_chain):
                abs_longest_chain = longest_chain
                matches = {word: "".join(longest_chain)}

            elif len(longest_chain) == len(abs_longest_chain):
                matches[word] = "".join(longest_chain)

    return matches


if __name__ == "__main__":
    results: Dict[str, str] = get_longest_ascending_alpha_chains(SCRABBLE_PATH)

    for key in results:
        print(f"Word: {key}")
        print(f"Chain: {results[key]}")
