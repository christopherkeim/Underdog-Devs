"""
Solution 7: 

Let's assign letters the following points:
    - W = 12
    - Z = 15
    - E = -17
    - All other letters = 1

What are all of the words with at least 50 points?


"""


from pathlib import Path

ROOT: Path = Path("More_Wordplay")
SCRABBLE_PATH: Path = ROOT / "tests" / "fixtures" / "sowpods.txt"


# Assumption 1: dataset is sorted alpha

# Assumption 2: all letters are homogenously cased

# Assumption 3: all inputs come from this dataset, no nonstring inputs, all valid


def load_data_from_file_as_dict(file_path: str) -> dict[str, int]:
    data: dict[str, int] = {}
    # Load the dataset into a data structure dict[str, int=0]
    with open(file_path, mode="r") as f:
        for line in f:
            token: str = line.strip()
            data[token] = 0

    return data


def get_all_50_point_words(scrabble_words: dict[str, int]) -> list[str]:
    # if needed, validate inputs for data type and values

    # Define letters with points dict[str, int]
    POINTS_DICT: dict[str, int] = {
        "W": 12,
        "Z": 15,
        "E": -17,
    }

    # initialize storage for final_matches list[str]
    final_matches: list[str] = []

    # Loop over every word in scrabble_words dataset
    for word_key in scrabble_words:
        # Loop over every letter, and count its score
        for letter in word_key:
            # if letter is W score += 12, etc
            if letter in POINTS_DICT:
                scrabble_words[word_key] += POINTS_DICT[letter]
            else:
                scrabble_words[word_key] += 1
        # if score >= 50
        if scrabble_words[word_key] >= 50:
            print(word_key, scrabble_words[word_key])
            # add it to final matches
            final_matches.append(word_key)

    # Return final matches
    return final_matches


def main() -> None:
    scrabble_words: dict[str, int] = load_data_from_file_as_dict(SCRABBLE_PATH)
    results: list[str] = get_all_50_point_words(scrabble_words)
    print(results)


if __name__ == "__main__":
    main()
