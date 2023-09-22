"""
Solution 5: What is the range of runtimes for the movies listed? 


Follow up: Distribution of runtimes for the movies listed, bucketed by half hour? 
"""


# Q1: Range = max and min?

# Note: Runtimes are strings formated in "int hour int minute"
#
# Q2: Are all values within "Runtimes" column identically formatted -
#     can I assume this data is valid as is?
from typing import List
from pathlib import Path
import csv

MOVIES_PATH: Path = Path("Movies/tests/fixtures/top_movies.csv")


def get_range_of_runtimes(path: Path) -> str:
    MINUTES_IN_HOUR: int = 60
    # Load this dataset into memory into a data structure
    with open(path, mode="r") as f:
        # Loop over each line in data structure holding dataset
        for idx, line in enumerate(csv.DictReader(f)):
            # extract out Runtimes column value for that line
            curr_runtime: List[str] = line["Runtime"].split()  # 2 hr 18 min
            print(curr_runtime)
            # convert it -> raw minutes
            hours: int = int(curr_runtime[0])
            minutes: int = 0

            if len(curr_runtime) > 2:
                minutes: int = int(curr_runtime[2])

            raw_minutes: int = (hours * MINUTES_IN_HOUR) + minutes

            if idx == 0:
                max_runtime: int = raw_minutes
                min_runtime: int = raw_minutes

            if raw_minutes > max_runtime:
                max_runtime = raw_minutes

            elif raw_minutes < min_runtime:
                min_runtime = raw_minutes

    result: str = f"""
    Range: {max_runtime - min_runtime} minutes
    Max: {max_runtime} minutes 
    Min: {min_runtime} minutes
    """
    # Return max, min, and range = (max-min)
    return result


if __name__ == "__main__":
    print(get_range_of_runtimes(MOVIES_PATH))
