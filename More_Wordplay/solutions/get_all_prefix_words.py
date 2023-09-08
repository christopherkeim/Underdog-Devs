"""
Solution 9: Write a function that takes a string prefix as an 
argument and returns an array of all of the words that start 
with that prefix (the prefix has to be at the beginning of 
the word)

"""


PREFIX_EXAMPLE: str = "PRE"

# Standard cases (begining), Fail (middle, end), Edge (x"pre")
EXAMPLES: list[str] = [
    " PREXXXXXXX",
    " PREXXXXXXX",
    " PREXXXXXXX",
    "PREXXXXXXX",  # standard
    "XXXXPREXXXX",  # fail (middle)
    "XXXXXXXXPRE",  # fail (end)
    "XPREXXXXXXX",  # edge
    " PREXXXXXXX",  # edge
    " PREXXXXXXX",
    " PREXXXXXXX",
    "PREXXXXXXX",
    "PREXXXXXXX",
    "IF",
    "",
]


def get_all_prefix_words(prefix: str, data: list[str]) -> list[str]:
    """"""

    # Measure the length of the prefix
    prefix_length: int = len(prefix)

    """
    Checking for inclusion in a matches collection.
    """
    return [
        word
        for word in set(data)
        if len(word) >= prefix_length
        if word[0:prefix_length] == prefix
    ]

    """
    Checking for condition to exclude, then condition to include.


    # storage for already compared words
    already_compared: set[str] = set()

    # Define storage for my matches list[str]
    matches: list[str] = [] 

    # Loop over every word in the dataset
    for word in set(data):
        if len(word) < len(prefix):
            continue
        # If the word[0:len(prefix)] == prefix
        if word[0:prefix_length] == prefix:
            # Add it to my matches
            matches.append(word)

    # Return matches
    return matches
    """


def main(test: bool = False) -> None:
    if test:
        scrabble_data: list[str] = EXAMPLES
        results: list[str] = get_all_prefix_words(PREFIX_EXAMPLE, scrabble_data)
        assert results == ["PREXXXXXXX"], results
        print(f"All tests passed: {results}")

    else:
        # scrabble_data: list[str] = load_data_from_file(SCRABBLE_PATH)
        results: list[str] = get_all_prefix_words(PREFIX_EXAMPLE, scrabble_data)
        print(results)


if __name__ == "__main__":
    main(True)
