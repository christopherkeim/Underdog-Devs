"""
Solution 1: What is the longest word where no letter is used more than once?
"""

# Q1: Is this dataset static - does it change in time?

# Q2: handle ties?

# Assumption 1: data is sorted

# Assumtpion 2: all letters are homogenously capitalized

# Note: write unit tests for this

from typing import List
from collections import defaultdict, Counter
from pathlib import Path


SCRABBLE_PATH: Path = Path("Bigger_Wordplay/tests/fixtures/sowpods.txt")


def get_longest_word_only_single_letters(path: Path) -> List[str]:
    # Initialize longest_length = 0
    longest_length: int = 0

    # initialize longest_word = None
    longest_words: List[str] = []

    # Loop through each line
    with open(path, mode="r") as f:
        # TEST THAT THIS SYNTAX STRIPS OUT \N
        for word in f:
            word = word.strip()
            # defaultdict, default value = 0
            intra_word_counts: defaultdict = defaultdict(lambda: 0)
            # state tracker
            valid_word: bool = True
            # for letter in line
            for letter in word:
                # for each letter found, increment count +1
                intra_word_counts[letter] += 1
                # if a letter has a count > 1
                if intra_word_counts[letter] > 1:
                    valid_word = False
                    break

            if not valid_word:
                continue

            curr_length: int = len(word)

            if curr_length > longest_length:
                # update longest_word = curr_word
                longest_words = [word]
                # update longest_legnth = curr_length
                longest_length = curr_length

            elif curr_length == longest_length:
                longest_words.append(word)

    return longest_words


def get_longest_word_only_single_letters_counter(path: Path) -> List[str]:
    # Initialize longest_length = 0
    longest_length: int = 0

    # initialize longest_word = None
    longest_words: List[str] = []

    # Loop through each line
    with open(path, mode="r") as f:
        for word in f:
            word = word.strip()
            # defaultdict, default value = 0
            intra_word_counts: Counter = Counter(word).most_common(1)[0][1]
            if intra_word_counts > 1:
                continue

            curr_length: int = len(word)

            if curr_length > longest_length:
                # update longest_word = curr_word
                longest_words = [word]
                # update longest_legnth = curr_length
                longest_length = curr_length

            elif curr_length == longest_length:
                longest_words.append(word)

    return longest_words


if __name__ == "__main__":
    print(get_longest_word_only_single_letters(SCRABBLE_PATH))
    print(get_longest_word_only_single_letters_counter(SCRABBLE_PATH))
