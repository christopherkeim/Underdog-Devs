"""
Solution 4: What is the earliest year on this list, and what 
were the films from that year?
"""

# Note: 7 columns total

# Q1: Are movie names unique across years

# Assumption 1: Movie titles themselves are unique

# Assumption 2: Release date column values are not unique

# Q2: Does the dataset change, or is it static

# Assumption 3: data is static

# In order to make comparisons - type cast Release Date -> int

from typing import List, Tuple, Dict
from pathlib import Path
import csv

MOVIES_PATH: Path = Path("Movies/tests/fixtures/top_movies.csv")


def get_earliest_year_and_films(path: Path) -> Tuple[int, List[str]]:
    earliest_year: int = 3000
    earliest_films: List[str] = None

    # Load this into memory as dictionary
    with open(path, mode="r") as f:
        # Loop through each line of this file
        for line in csv.DictReader(f):
            # Extract the Release Date
            release_date: int = int(line["Release Date"])
            # Extract the title
            current_title: str = line["Title"]

            if release_date < earliest_year:
                # update earliest_year
                earliest_year = release_date
                # overwrite films list -> with [current_film]
                earliest_films = [current_title]

            elif release_date == earliest_year:
                # append current_film to films list
                earliest_films.append(current_title)

        return earliest_year, earliest_films


if __name__ == "__main__":
    print(get_earliest_year_and_films(MOVIES_PATH))
