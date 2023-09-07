"""
Solution 8: Write a function that takes a string substring as 
an argument and returns an array of all of the words that contain 
that substring (the substring can appear anywhere in the word).

"""

# Assumption 1: the dataset is sorted alphabetically

# Q2: Does the case have to match?
# Assumption 2: All words are homogenously cased (UPPERCASE)

# Q3: Clarify any vagueness in the prompt
# Assumption 3: Position of substring doesn't have to be fixed within word

# Q4: Ask but, doesn't really matter for problem - for curiosity
# Assumption 4: All characters are A-Z (no special characters)

# Here you've already interogated your edge cases a bit - this is info gathering
# for thinking of tests - here propose some examples after you've gathered info

# Precision: What do I need to worry about vs. what do I not need to worry about

from pathlib import Path

ROOT: Path = Path("More_Wordplay")
SCRABBLE_PATH: Path = ROOT / "tests" / "fixtures" / "sowpods.txt"


def load_data_from_file_as_list(file_path: str) -> list[str]:
    # Load this data into memory list[str]
    with open(file_path, mode="r") as f:
        data: list[str] = f.read().splitlines()

    return data


"""
Testing goal: be as minimal as possible while picking up all or many of 
cases that could come up [standard (beginning, middle, end), failure (not present),
edge(all but one character)]


Choose the smallest example that will get the job done

Always assume you only have time for one example - choose the one that is the most
likely to fail (binary pass or fail) - that you're least confident with so you 
flush out your bugs early and fix them 

Think high level about creating strong signals that pass through your 
function and illuminate bugs - tracer dye

"""
# ubiquitous positive example
SUBSTRING_EXAMPLE1: str = "UNIQUE"

# null negative example
SUBSTRING_EXAMPLE2: str = "NULL"


EXAMPLES1: list[str] = [
    "UNIQUEXXXXX",  # Standard (beginning)
    "XXXXXUNIQUEXXXXX",  # Standard (middle)
    "XXXXXUNIQUE",  # Standard (end)
    "XXXXXXXXXX",  # Fail (not present)
    "OOOOOUNIQOOOOO",  # Edge (all but one char)
]


def get_all_containing_substring(substring: str, data: list[str]) -> list[str]:
    """
    This function takes a target substring and dataset as
    inputs and returns a list of strings from that dataset
    containing the target substring.
    """
    # Initialize storage for any matches list[str]
    matches: list[str] = []
    # Loop over ever word in scrabble_words
    for word in data:
        # If this substring is present in the word
        if substring in word:
            # Add this word to my matches
            matches.append(word)

    # Return matches
    return matches


def main(test: bool = False) -> None:
    if test:
        scrabble_words: list[str] = EXAMPLES1

    else:
        scrabble_words: list[str] = load_data_from_file_as_list(SCRABBLE_PATH)

    results: list[str] = get_all_containing_substring(
        SUBSTRING_EXAMPLE1, scrabble_words
    )

    print(results)


if __name__ == "__main__":
    main()
