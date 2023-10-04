"""
Solution 6: Finding alphabet chains:
    - First, what are all of the words that have a least one “A”, one “B”, 
      one “C”, one “D”, one “E”, and one “F” in them, in any order?
        - For example, “FEEDBACK” is an answer to this question

    - Next, is “ABCDEF” the longest alphabet chain that can be found in a
      word, or is there a longer chain starting somewhere else in the alphabet? 
      Find the longest chain and the words that can be made from that chain.
"""

# Q1: Exact definition of alphabet chain?

# Assumption 1: an alphabet chain is present in a word if that word
# contains letters contiguous in the alphabet: “FEEDBACK” is composed of
# an alphabet chain because it contains the letters "ABCDEF"


from typing import List, Tuple, Set, Dict
from pathlib import Path


SCRABBLE_PATH: Path = Path("Bigger_Wordplay/tests/fixtures/sowpods.txt")
TEST_PATH: Path = Path("Bigger_Wordplay/tests/fixtures/chain_test.txt")


def load_data_from_file(path: Path) -> List[str]:
    with open(path, mode="r") as f:
        data: List[str] = f.read().splitlines()

    return data


def get_all_one_abcdef_words(data: List[str]) -> List[str]:
    LETTERS: Set[str] = {"A", "B", "C", "D", "E", "F"}

    # Initalize a list to hold matches
    matches: List[str] = []

    for word in data:
        if LETTERS.issubset(set(word)):
            matches.append(word)
    return matches


def get_longest_alpha_chain(data: List[str]) -> List[List[str]]:
    """
    Discoveres the longest aphabet chain within a dataset and returns it
    as a list of characters.
    """
    # Longest chains discovered globally in dataset handling ties
    abs_longest_chains: List[List[int]] = [[]]
    # Loop over every word in the dataset
    for word in data:
        # Convert the word to a set of unique characters for max sort of 26 char;
        # then compute ord values for each unique character and sort ascending
        char_ords: List[int] = sorted(ord(letter) for letter in set(word))

        # Longest chain within word
        longest_intra_chain: List[int] = []
        # Comparison of discovered chains within word
        working_word_chain: List[int] = []

        # Loop over each sorted character ord value
        for letter in char_ords:
            # Initialization branch
            if len(longest_intra_chain) == 0:
                working_word_chain = [letter]
            # Chain building branch
            elif letter == working_word_chain[-1] + 1:
                working_word_chain.append(letter)
            # Stop and restart branch
            else:
                working_word_chain = [letter]

            # Update longest_intra_chain
            if len(working_word_chain) > len(longest_intra_chain):
                longest_intra_chain = working_word_chain

        # Update global longest chain in dataset handling ties
        if len(longest_intra_chain) > len(abs_longest_chains[0]):
            abs_longest_chains = [longest_intra_chain]

        elif len(longest_intra_chain) == len(abs_longest_chains[0]):
            abs_longest_chains.append(longest_intra_chain)

    # Convert the ord values back to strings
    for i in range(len(abs_longest_chains)):
        abs_longest_chains[i] = [chr(o) for o in abs_longest_chains[i]]

    return abs_longest_chains


def get_all_words_made_from_alpha_chain(
    data: List[str], alpha_chain: List[str]
) -> Tuple[str, List[str]]:
    """
    Parses the dataset and returns all of the words that are composable
    from the input alpha chain.
    """
    letter_set: Set[str] = set(alpha_chain)
    matches: List[str] = []
    for word in data:
        if letter_set.issubset(set(word)):
            matches.append(word)

    alpha_chain_str: str = "".join(letter for letter in alpha_chain)

    return alpha_chain_str, matches


if __name__ == "__main__":
    # Section 1: discover all words containing "A", "B", "C", "D", "E", "F"
    data: List[str] = load_data_from_file(SCRABBLE_PATH)
    result: List[str] = get_all_one_abcdef_words(data)

    # Section 2: Discover the longest alphabet chain and words that can be made
    # from that chain
    longest_chains: List[List[str]] = get_longest_alpha_chain(data)

    results: Dict[str, List[str]] = {}
    for chain in longest_chains:
        alpha_chain_str, words = get_all_words_made_from_alpha_chain(data, chain)
        results[alpha_chain_str] = words

    for chain_str in results:
        print(f"Longest alpha chain: {chain_str}")
        print(f"Words: {results[chain_str]}")
