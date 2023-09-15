"""
Solution 4: Print out a ranking of who has won the MVP more than once, by times 
won, e.g. this output:

    - 6 times: Michael Jordan
    - 3 times: Shaquille O'Neal, LeBron James
    - 2 times: <etc>

"""
# Need to load dataset into memory, extract out 5th column, count


from collections import defaultdict
from pathlib import Path
import csv


NBA_PATH: Path = Path("NBA/tests/fixtures/nba_finals.csv")


def load_csv_as_dict(path: str) -> dict[str, int]:
    mvps: defaultdict = defaultdict(lambda: 0)

    with open(path, mode="r") as f:
        for row in csv.DictReader(f):
            mvp: str = row["MVP"]
            if mvp != "":
                mvps[mvp] += 1

    return mvps


def rank_mvps_by_more_than_1_win(mvps: dict[str, int]) -> None:
    # initialize an empty sorted_dict default dict
    unsorted_dict: defaultdict = defaultdict(list)
    # Loop over each key in this dictionary
    for key in mvps:
        # Extract name
        name = key
        # Extract the count value
        count = mvps[key]
        if count > 1:
            unsorted_dict[count].append(name)

    results: list[int] = sorted(unsorted_dict, reverse=True)

    for count in results:
        print(f"{count} time: {', '.join(unsorted_dict[count])}")


if __name__ == "__main__":
    mvps = load_csv_as_dict(NBA_PATH)
    results = rank_mvps_by_more_than_1_win(mvps)
