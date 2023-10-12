"""
Solution 6: Finding alphabet chains:

    - Next, is “ABCDEF” the longest alphabet chain that can be found in a
      word, or is there a longer chain starting somewhere else in the alphabet? 
      Find the longest chain and the words that can be made from that chain.
"""

# Assumption 1: an alpha chain is a series of letters present in a word
# that are contiguous within the alphabet -> for example, "FEEDBACK" contains
# "ABCDEF"


# Note: "ABCDEF" constitutes an alpha chain and "FEEDBACK" is a positive match for
# this chain because it contains those letters in any order

from typing import Tuple, List
from pathlib import Path

SCRABBLE_PATH: Path = Path("Bigger_Wordplay/tests/fixtures/sowpods.txt")


def get_longest_alpha_chains(path: Path) -> Tuple[List[str], List[str]]:
    # absolute_longest_alpha_chains = [[]]
    abs_longest_alpha_chains: List[List[str]] = [[]]
    # abs_longest_length
    abs_longest_length: int = 0
    # words_from_global chain = [""]
    abs_matches: List[str] = []

    cycles: int = 0
    # Loop over each word in the dataset
    with open(path, mode="r") as f:
        for word in f:
            cycles += 1
            word: str = word.strip()

            # distill out the unique letters, convert them into ASCII integer values,
            # sort them ascending
            sorted_ords: List[str] = sorted(char for char in set(word))

            if len(sorted_ords) < abs_longest_length:
                continue

            working_chain: List[str] = []

            # Loop over each letter
            for idx, letter in enumerate(sorted_ords):
                cycles += 1

                if len(sorted_ords[idx:]) + len(working_chain) < abs_longest_length:
                    break

                # Initialization condition
                if len(working_chain) == 0:
                    working_chain.append(letter)

                # Chain building condition
                elif ord(letter) == ord(working_chain[-1]) + 1:
                    working_chain.append(letter)

                # Reset condition
                else:
                    working_chain = [letter]

            # is longest_intra_word_chain > global chain
            if len(working_chain) > len(abs_longest_alpha_chains[0]):
                abs_longest_alpha_chains = [working_chain]
                abs_longest_length = len(working_chain)
                abs_matches = [word]

            # is longest_intra_word_chain == global chain
            elif len(working_chain) == len(abs_longest_alpha_chains[0]):
                # append longest_intra_word_chain to global chains
                abs_longest_alpha_chains.append(working_chain)
                abs_matches.append(word)

    print(cycles)

    # return global chains + words that match them
    return abs_longest_alpha_chains, abs_matches


if __name__ == "__main__":
    longest_chains, words = get_longest_alpha_chains(SCRABBLE_PATH)

    for idx in range(len(longest_chains)):
        print(f"Word: {words[idx]}")
        print(f"Chain: {longest_chains[idx]}")
