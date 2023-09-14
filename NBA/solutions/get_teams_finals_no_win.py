"""
Solution 3: Which teams have made it to the NBA finals but have never won?
"""

# Q1: is this dataset complete ?(dataset doesn't change)

# Assumption 1: don't need to worry about validation between parsing events

# Q2: [] if no teams?

# Q3: if 2 teams tie - who is considered winner?

from pathlib import Path
import csv


NBA_PATH: Path = Path("NBA/tests/fixtures/nba_finals.csv")


def get_teams_finals_no_win(path: Path) -> set[str]:
    winners: set[str] = set()
    losers: set[str] = set()

    with open(path, mode="r") as f:
        reader = csv.reader(f)
        # Loop through each line of csv file
        for idx, line in enumerate(reader):
            if idx == 0:
                continue
            # extract line[1] (winner)
            winner = line[1]
            # extract line[2] (loser)
            loser = line[2]
            # add these values into separate sets
            winners.add(winner)
            losers.add(loser)
    # Extract team names that appear only in losers set (not present in winner set)
    # using set.difference()
    matches: set[str] = losers.difference(winners)
    # return the losers
    return matches


if __name__ == "__main__":
    print(get_teams_finals_no_win(NBA_PATH))
