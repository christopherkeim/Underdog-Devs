"""
Solution 1: What are all of the words that have only “U”s for vowels?
"""
import os
import logging


logger: logging.RootLogger = logging.getLogger()

logging.basicConfig(level=logging.INFO)


# Assumption 1: dataset is sorted already

# Assumption 2: all words within dataset are valid unicode words

# Note: dataset is ~ 256k words


SCRABBLE_PATH: str = "More_Wordplay/tests/fixtures/sowpods.txt"


def load_data_from_file(file_path: str) -> set[str]:
    """
    This function takes a path to a file as input and returns
    that file loaded into memory as a set[str]
    """
    # make sure that this file exists

    with open(file_path, mode="r") as f:
        data: set[str] = set(f.read().splitlines())

    return data


def get_only_u_vowels() -> set[str]:
    """ """

    # load our data into a set[str]
    scrabble_words: set[str] = load_data_from_file(SCRABBLE_PATH)

    # validation for data type

    # validation for values (i.e. no "" or other objects)

    # define a list of vowels
    VOWELS: set[str] = {"A", "E", "I", "O", "U"}
    # initialize a data structure my matches set[str]
    matches: set[str] = set()

    # Loop through each word in this dataset
    for word in scrabble_words:
        # Intra word vowel tracker set[str]
        intra_word_vowels: set[str] = set()
        # Check each letter in the word
        for letter in word:
            # If this word is a vowel add it to our intra word vowels tracker
            if letter in VOWELS:
                intra_word_vowels.add(letter)
        # If this word has only the vowel == "U"
        if len(intra_word_vowels) == 1 and "U" in intra_word_vowels:
            # Add this word to the matches set
            matches.add(word)

    # Return matches
    return matches


if __name__ == "__main__":
    print(os.getcwd())
    print(get_only_u_vowels())
