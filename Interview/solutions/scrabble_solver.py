"""
Part 1

Write code that:

- Accepts a string (e.g. as an argument to a function, or as a command-line argument). 
This string represents your Scrabble “rack”.
- Prints out the words that can be made from the characters in that input string, 
along with their Scrabble scores, one word per line, in descending score order

Example input and output:

`$ python scrabble_cheater.py SPCQEIU  # Use any language you like.`
`17 piques`
`17 equips`
`16 quips`
`16 pique`
`16 equip`
`15 quip`
`…`

Key points:

- Letters cannot be reused. For example, if your Scrabble rack is “ABCD”, you 
can make the word “CAB” but not the word “DAD”, because you only have one “D”.


Part 2

Extend the script to handle blank tiles. When reading the input, the character _ 
can be used as a wildcard — it can represent any letter.

Wildcards do not count towards a word's score.

NOTE:

Reading 2 data sources into memory

1) Check input string characters against scrabble words
    - is it a substring of any combination of the given rack string
    - only need existence and less frequency of given characters in rack string
2) score them - take frequencies within substring hash and multiply them against
   with scores in score has

Part 2: adding 1 more letter to "rack" that represents ANY char
-> this extends the collection of valid words allowing any extra letter or
   1 present letters with +1 frequency

Test Cases:
AA <- edge
AAA 
"""
from typing import List, Tuple, Dict
from pathlib import Path
import json
from collections import Counter
import sys


SCRABBLE_PATH: Path = Path("Interview/tests/fixtures/sowpods.txt")
SCORES_PATH: Path = Path("Interview/tests/fixtures/letter_scores.txt")


def load_data_from_file() -> List[str]:
    with open(SCRABBLE_PATH, mode="r") as f:
        data: List[str] = f.read().splitlines()

    return data


def load_scores_from_file() -> Dict[str, int]:
    with open(SCORES_PATH, mode="r") as f:
        data: str = f.read().split("=")[1].upper()
        data: Dict[str, int] = json.loads(data)

    return data


def scrabble_solver(rack: str = "SPCQEIU") -> None:
    # Validation for CLI arg
    if len(sys.argv) != 2:
        raise ValueError("Takes one argument 'scrabble rack'")

    if not isinstance(sys.argv[1], str):
        raise TypeError("scrabble rack argument must be a string")

    rack: str = sys.argv[1].upper()

    # Load data from file assets
    SCRABBLE_WORDS: List[str] = load_data_from_file()
    SCORES: Dict[str, int] = load_scores_from_file()

    # Storage for results
    results: List[Tuple[int, str]] = []

    # Load rack into a hash map
    rack_dict: Dict[str, int] = dict(Counter(rack).items())

    # Loop over each word in scrabble dataset
    for word in SCRABBLE_WORDS:
        # Read word into hash map
        word_dict: Dict[str, int] = dict(Counter(word).items())

        # State and score initialization for word
        is_valid: bool = True
        score: int = 0
        wild_card_count: int = rack_dict["_"] if "_" in rack_dict else 0

        # Two dictionaries (rack and word)
        for letter_key in word_dict:
            # Check for presence and frequency in rack
            if (
                letter_key not in rack_dict
                or rack_dict[letter_key] < word_dict[letter_key]
            ):
                # Wildcard
                if wild_card_count > 0:
                    # Duplicate letter handling
                    if wild_card_count < word_dict[letter_key]:
                        is_valid = False
                        break

                    wild_card_count -= word_dict[letter_key]

                    continue

                is_valid = False
                break

            score += SCORES[letter_key] * word_dict[letter_key]

        if is_valid:
            results.append((score, word))

    sorted_results: List[Tuple[int, str]] = sorted(results, reverse=True)

    for score, word in sorted_results:
        print(score, word)

    print(len(sorted_results))


if __name__ == "__main__":
    scrabble_solver()
