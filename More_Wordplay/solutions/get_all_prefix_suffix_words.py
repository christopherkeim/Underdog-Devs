"""
Solution 10: Write a function that takes a string prefix as the 
first argument, a string suffix as the second argument, and an 
integer length as the third argument. It should return an array of 
all of the words that start with that prefix, end with that 
suffix, and are that length

"""


# Empty suffix length 0

# Empty prefix of length 0

# Is the length argument > 0 ?

# No words found = []

# Testing: pass cases, fail cases, edge cases

PREFIX_EXAMPLE: str = "PRE"

SUFFIX_EXAMPLE: str = "FIX"

LENGTH_EXAMPLE: int = 7

TEST_EXAMPLES: list[str] = ["PREXFIX", "XXXOXX", "PRXXFIX", "PREXXIX", "PREXXFIX", ""]


def get_all_prefix_suffix_length_words(
    prefix: str, suffix: str, length: int, data: list[str]
) -> list[str]:
    # measure prefix length
    prefix_length: int = len(prefix)

    # measure suffix length
    suffix_length: int = len(suffix)

    # Initialize storage for matches
    matches: list[str] = []

    # Loop over every word in dataset
    for word in data:
        if len(word) != length:
            print(f"Length failure: {word}")

            continue

        if word[0:prefix_length] != prefix:
            continue

        if word[-suffix_length:] == suffix or suffix_length == 0:
            print(f"All pass: {word}")

            matches.append(word)

    # return the matches
    return matches


def main(test: bool = False) -> None:
    if test:
        scrabble_words: list[str] = TEST_EXAMPLES
        results: list[str] = get_all_prefix_suffix_length_words(
            PREFIX_EXAMPLE, SUFFIX_EXAMPLE, LENGTH_EXAMPLE, scrabble_words
        )
        assert results == ["PREXFIX"], results
        print("Test passed.")


if __name__ == "__main__":
    main(True)
