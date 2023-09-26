"""
Solution 2: What song was the #1 song for the most weeks of 
2000, who was the artist, and how many weeks was it at #1?
"""

# Song with rank == 1 for most amount of weeks - count this

# Q1: Are song names unique - can I assume if song1 has the name
#     "With Arms Wide Open" all other instances of song1 have that name?

# Assumption1: song names are unique

# Assumption2: date column is in weeks rather than days

# Q2: is this dataset static, or does it constantly change in time?

from typing import Tuple
from collections import defaultdict
from pathlib import Path
import csv


BB_PATH: Path = Path("Billboard/tests/fixtures/billboard100_2000.csv")


def get_number_one_song_for_most_weeks(path: Path) -> Tuple[str, str, int]:
    matches: defaultdict = defaultdict(lambda: 0)
    number_one_song: str = None
    number_one_artist: str = None

    # Loop over each line of this file
    with open(path, mode="r") as f:
        for line in csv.DictReader(f):
            # extract out the "rank"
            curr_rank: int = int(line["rank"])

            # If this song's rank is not 1, move on
            if curr_rank != 1:
                continue

            # extract out the "song"
            curr_song: str = line["song"]

            # Count this song
            matches[curr_song] += 1

            # Update number_one_song and number_one_artist
            if matches[curr_song] > matches[number_one_song] or number_one_song is None:
                number_one_song = curr_song
                number_one_artist = line["artist"]

    # Return #1 song and artist for the most weeks of 2000
    return number_one_song, number_one_artist, matches[number_one_song]


if __name__ == "__main__":
    song, artist, weeks = get_number_one_song_for_most_weeks(BB_PATH)
    print("The #1 song and artist for the most weeks in 2000 is: \n")
    print(f"Song: {song}\nArtist: {artist}\nWeeks: {weeks}")
