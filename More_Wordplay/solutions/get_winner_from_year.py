"""
Solution 14: Write a function that takes as an argument a year and 
returns the winner of the NBA finals that year
"""

# Q1: Does each year have a valid winner value

# Assumption 1: Code should handle potential invalid year or winner values ("")

from pathlib import Path
import csv

TEST_DICT: dict[str, str] = {
    "1990": "Carol",
    "2022": "Bob",
    "2000": "",  # -> ""
    "": "",  # -> ""
}


# Load using builtin csv -> list[list] -> hash map for O(1) search
NBA: Path = Path("./More_Wordplay/tests/fixtures/nba_finals.csv")


def load_csv_as_dict(path: Path) -> dict[str, str]:
    with open(path, mode="r") as f:
        nba_dict = {}
        reader = csv.reader(f)
        for line in reader:
            nba_dict[line[0]] = line[1]

    return nba_dict


def get_winner_from_year(year: str, test: bool = False) -> str:
    if test:
        nba_dict = TEST_DICT
    else:
        nba_dict: dict[str, str] = load_csv_as_dict(NBA)

    try:
        return nba_dict[year]

    except KeyError:
        return "Key not in dataset."


# ingest key

# return the year
if __name__ == "__main__":
    result1: str = get_winner_from_year("1990", test=True)
    assert result1 == "Carol"

    result2: str = get_winner_from_year("2022", test=True)
    assert result2 == "Bob"

    result3: str = get_winner_from_year("2000", test=True)
    assert result3 == ""

    result4: str = get_winner_from_year("", test=True)
    assert result4 == ""

    result5: str = get_winner_from_year("2009")
    assert result5 == "Los Angeles Lakers"

    result6: str = get_winner_from_year("3000")
    assert result6 == "Key not in dataset."

    print("SUCCESS!!!!!!!!!!!!!!!!!!!!!!!")
