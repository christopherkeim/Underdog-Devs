"""
Solution 4: What song(s) were on the charts (anywhere on the charts) 
for the most weeks of 2000?
"""

# Q1: Are "date" values unique? And if so - does each "date" value enocde
#     a different week

# Assumption 1: ^ this is true

# Q2: Can I assume that values in this dataset for each column are unique?
# Assumption 2: song values are unique

# Q3: Does this dataset change in time, or is it static?
# Assumption3: its static

# Q4: do I handle ties? - will handle these

from typing import List
from collections import defaultdict
from pathlib import Path
import csv

BB_PATH: Path = Path("Billboard/tests/fixtures/billboard100_2000.csv")


def get_songs_on_chart_with_most_weeks(path: Path) -> List[str]:
    # instantiate a default dictionary, default = 0
    songs: defaultdict = defaultdict(lambda: 0)

    # songs_with_most_weeks = []
    songs_with_most_weeks: List[str] = []

    # Loop over each line in this csv file
    with open(path, mode="r") as f:
        for line in csv.DictReader(f):
            # Extract the current "song"
            curr_song: str = line["song"]
            # incrememnt this song's count
            songs[curr_song] += 1

            if len(songs_with_most_weeks) == 0:
                songs_with_most_weeks.append(curr_song)

            if songs[curr_song] > songs[songs_with_most_weeks[0]]:
                songs_with_most_weeks = [curr_song]

            elif (
                songs[curr_song] == songs[songs_with_most_weeks[0]]
                and curr_song not in songs_with_most_weeks
            ):
                songs_with_most_weeks.append(curr_song)

        return songs_with_most_weeks, songs


if __name__ == "__main__":
    song_names, songs = get_songs_on_chart_with_most_weeks(BB_PATH)
    for k, v in sorted(songs.items(), key=lambda x: x[1]):
        print(k, v)
