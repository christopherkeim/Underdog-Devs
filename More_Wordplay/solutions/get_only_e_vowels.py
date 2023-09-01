"""
Solution 2: What are all of the words that have only “E”s for vowels 
and are at least 15 letters long?

Note: try to find out upfront if you should optimize.
"""

# Assumptions 1: this dataset is order / sorted

# Assumption 2: all words are completely uppercase

# Assumption 3: Every word in this data is a valid unicode word

SCRABBLE_PATH: str = "More_Wordplay/tests/fixtures/sowpods.txt"

TEST_EXAMPLES: list[str] = [
    "SWPYTCBDHFKLJKFDQ",
    "EEEEEEEEEEEEEEE",
    "ABRA",
    "EEEEEEEAFHGJYKMC",
]


def runner(test: bool = False) -> list[str]:
    if test:
        results: list[str] = get_only_e_vowels(TEST_EXAMPLES)
    else:
        # Load this dataset into memory as a data structure
        scrabble_words: list[str] = load_data_from_file(SCRABBLE_PATH)
        # Call our search function
        results: list[str] = get_only_e_vowels(scrabble_words)

    return results


def load_data_from_file(file_path: str) -> list[str]:
    # Check that the file exists
    with open(file_path, mode="r") as f:
        data: list[str] = f.read().splitlines()

    return data


def get_only_e_vowels(scrabble_words: list[str]) -> list[str]:
    """ """

    # validate data type is correct

    # validate that the values are correct (no "" or other objects)

    # hold vowels in a variable set[str]
    BAD_VOWELS: set[str] = {"A", "I", "O", "U"}
    # hold matches in a set[str]
    matches: list[str] = []
    # Loop through each word in the dataset
    for word in scrabble_words:
        # measure the length of word, if < 15 continue
        if len(word) < 15:
            continue
        # Initialize the state of our word as invalid
        valid_word: bool = False
        # Loop through each letter in this word
        for letter in word:
            # If this letter is a bad vowel
            if letter in BAD_VOWELS:
                # Move onto the next word
                valid_word: bool = False
                break
            # Tentatively set this word's state to valid and move onto next letter
            if letter == "E":
                valid_word: bool = True

        # If this word has passed all of our checks for desired state add it to matches
        if valid_word:
            matches.append(word)

    # Return matches
    return matches


if __name__ == "__main__":
    print(runner())
