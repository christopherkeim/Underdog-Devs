"""
Solution 2: What is the highest grossing movie from Universal Pictures, domestically?
"""

# Look at US Sales, extract Title with highest int value

# Q1: What is datatype of US Sales column? -> int

# Q2: Can I assume that this dataset is complete and static? -> does
#     the dataset get updated on a time cycle

#    - control for null values?

# Q3: Any runtime or memory constraints to consider?

# Q4: is the string "Universal Pictures" the standard ID for Universial Pictures
#     within column?


from typing import Tuple
from pathlib import Path
import csv

MOVIES_PATH: Path = Path("Movies/tests/fixtures/top_movies.csv")

DISTRIBUTOR: str = "Universal Pictures"


def get_universal_pictures_domestic(distributor: str) -> Tuple[int, str]:
    # Load this data into memory as a dictionary of move_names: US Sales pairs

    top_movie = None
    highest_sales: int = 0

    with open(MOVIES_PATH, mode="r") as f:
        for idx, line in enumerate(csv.reader(f)):
            if idx == 0:
                continue
            # If the distributor == DISTRIBUTOR
            if line[1] == distributor:
                # Extract the name
                curr_movie_name: str = line[0]
                # Extract the US Sales
                curr_sales: int = int(line[3])

                # if current_sales > highest_sales
                if curr_sales > highest_sales:
                    # update top_movie
                    top_movie = curr_movie_name
                    # update highest_sales
                    highest_sales = curr_sales

    return top_movie, highest_sales


if __name__ == "__main__":
    print(get_universal_pictures_domestic(DISTRIBUTOR))
    print(get_universal_pictures_domestic("Walt Disney Studios Motion Pictures"))
