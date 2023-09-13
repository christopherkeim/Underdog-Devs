"""
Solution 2: Write a function that takes as an argument a team name 
and returns an array of all of the years the team has won the NBA finals.
"""

# Q: Do all team names have winning years -> handle key errors as "didn't win"

# always think about edge case first - how can you break it


from pathlib import Path
import csv


TEST_NAME1: str = "Miami Heat"
TEST_NAME2: str = "asdfj;sldfjlka"
TEST_NAME3: str = "Winner"

# load this into memory as a dict[team name, [winning years]] key value pairs

NBA_PATH: Path = Path("NBA/tests/fixtures/nba_finals.csv")


def load_csv_into_dict(path: Path) -> dict[str, list[str]]:
    team_wins: dict[str, list[str]] = {}

    with open(path, mode="r") as f:
        """TODO: implement remove header or skip over header columns first row"""
        reader = csv.reader(f)
        for line in reader:
            name = line[1]
            winning_year = line[0]

            if name in team_wins:
                team_wins[name].append(winning_year)

            else:
                team_wins[name] = [winning_year]

    return team_wins


def get_winning_year_from_team_name(name: str) -> list[str]:
    # load the data into a variable
    data: dict[str, list[str]] = load_csv_into_dict(NBA_PATH)

    # Validation for key errors
    try:
        result: list[str] = data[name]
    except KeyError:
        return ["Name not in winners."]

    return result


if __name__ == "__main__":
    print(get_winning_year_from_team_name(TEST_NAME1))
    print(get_winning_year_from_team_name(TEST_NAME2))
    print(get_winning_year_from_team_name(TEST_NAME3))
