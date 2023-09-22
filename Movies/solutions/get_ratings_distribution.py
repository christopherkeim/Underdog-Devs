"""
What is the distribution of ratings? (How many are PG, PG-13, R, etc.?) 
"""

# Assumption1: ratings values are unique

# Q1: are there other rating values (aliases, such as nc17, G than above ^)

# Q2: does the real dataset change in time?
from typing import List
from pathlib import Path
from collections import defaultdict
import csv


MOVIES_PATH: Path = Path("Movies/tests/fixtures/top_movies.csv")


def get_ratings_distribution(path: Path) -> defaultdict:
    # Instaniate a defaultdict count = 0
    ratings_distribution: defaultdict = defaultdict(int)

    # Load dataset into memory - hash map
    with open(path, mode="r") as f:
        # Loop over each line of the file
        for line in csv.DictReader(f):
            # extract out the value in ratings column
            current_rating: str = line["Rating"]

            ratings_distribution[current_rating] += 1

    return ratings_distribution


if __name__ == "__main__":
    distr: defaultdict = get_ratings_distribution(MOVIES_PATH)
    sorted_distr: List = sorted(distr, key=lambda x: distr[x])
    for rating in sorted_distr:
        print(f"{rating}: {distr[rating]}")
