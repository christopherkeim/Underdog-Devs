"""
Solution 3: What distributor has the most films on this list? 
"""

# Note: 7 columns total


# Q1: Are distributor names standardized - the same distributor has
#     the same name across instances (no abbreviations, etc.)
# Assumption1: yes
# Q2: Is each title unique?
# Assumption 2: Each movie title is present in a distinct year (unique id)

from collections import Counter
from typing import List, Dict, Tuple
from pathlib import Path
import csv

MOVIES_PATH: Path = Path("Movies/tests/fixtures/top_movies.csv")


def get_distributor_with_most_films(path: Path) -> Tuple[str, int]:
    best_distributor: str = None
    most_films: int = 0
    distributor_counts: Dict[str, int] = {}

    with open(path, mode="r") as f:
        for line in csv.DictReader(f):
            dist = line["Distributor"]

            if dist in distributor_counts:
                distributor_counts[dist] += 1
            else:
                distributor_counts[dist] = 1

            if distributor_counts[dist] > most_films:
                most_films = distributor_counts[dist]
                best_distributor = dist

    return best_distributor, most_films


def load_data_from_csv(path: Path) -> List[Dict[str, str]]:
    with open(path, mode="r") as f:
        data = list(csv.DictReader(f))

    return data


def extract_column_by_name(
    dataset: List[Dict[str, str]], column_name: str
) -> List[str]:
    extracted_column = []
    for line in dataset:
        item: str = line[column_name]
        extracted_column.append(item)
    return extracted_column


def count_titles(data: List[Dict[str, str]]) -> Dict[str, int]:
    titles = extract_column_by_name(data, "Title")
    title_counts = Counter(titles)
    if all(title_counts[key] == 1 for key in title_counts):
        print(True)
    else:
        print(False)

    total_counts = sum(title_counts.values())
    return total_counts


if __name__ == "__main__":
    data = load_data_from_csv(MOVIES_PATH)

    # First assumption test
    distributors: List[str] = extract_column_by_name(data, "Distributor")
    for dist in sorted(set(distributors)):
        print(dist)

    # Second assumption test
    total_counts = count_titles(data)

    unique_titles = {(row["Title"], row["Release Date"]) for row in data}

    assert len(unique_titles) == total_counts, "Not unique!!!"

    print("They're unique!!!")

    # Solution
    distributor, film_count = get_distributor_with_most_films(MOVIES_PATH)

    print(distributor, film_count)
