"""
Solution 3: What are all of the words that start with “PRO”, 
end in “ING”, and are exactly 11 letters long?

Assumption 1: each line is uppercased 

Assumption 2: data is already sorted 

Assumption 3: total size of dataset is ~ 267k * avg word length in (bytes) 

Assumption 4: all characters as ASCII


"""

# Test cases 1 pass, 1 obvious fail, 1 edge case, 1 threshold close
TEST_EXAMPLES: list[str] = ["PROXXXXXING", "ABA", "PPROXXXXING", "GNIXXXXXORP"]


SCRABBLE_PATH: str = "More_Wordplay/tests/fixtures/sowpods.txt"


def runner(test: bool = False) -> list[str]:
    # Runner for testing
    if test:
        results: list[str] = get_start_pro_end_ing_11(TEST_EXAMPLES)
    else:
        # Load this dataset into memory as a data structure
        scrabble_words: list[str] = load_data_from_file(SCRABBLE_PATH)
        # Call our filter function
        results: list[str] = get_start_pro_end_ing_11(scrabble_words)

    return results


def load_data_from_file(file_path: str) -> list[str]:
    # Load this dataset into memory as a data structure list[str]

    # Make sure the files exists

    with open(file_path, mode="r") as f:
        data: list[str] = f.read().splitlines()

    return data


def get_start_pro_end_ing_11(scrabble_words: list[str]) -> list[str]:
    # Filter function

    # Validate that data type is correct
    if not isinstance(scrabble_words, list) or not all(
        isinstance(word, str) for word in scrabble_words
    ):
        raise TypeError("This function requires a list of strings as input.")

    # Validate that the values are correct
    if not all((len(word) > 0) for word in scrabble_words):
        raise ValueError("This function requires valid strings.")

    # Initialize a data structure to store our matches list[str]
    matches: list[str] = []
    # loop through each word
    for word in scrabble_words:
        # If the word is not exactly 11 characters long move onto the next word
        if len(word) != 11:
            continue
        # If it is 11 chars, starts with PRO, ends with ING add to matches
        if "PRO" == word[0:3] and "ING" == word[-3:]:
            matches.append(word)

    # Return our matches
    return matches


if __name__ == "__main__":
    print(runner())
