"""
Solution 3: What artist had the most songs chart in 2000, and what were 
those songs?
"""

# Q1: Is this dataset static - does this dataset change in time (daily, hourly...)?

# Q2: Can I assume that artist names are unique?

# Assumption 1: dataset is static

# Assumption 2: artist names are unique

from typing import Tuple, Set
from collections import defaultdict
from pathlib import Path
import csv

BB_PATH: Path = Path("Billboard/tests/fixtures/billboard100_2000.csv")


def get_artists_with_most_songs(path: Path) -> Tuple[str, Set[str]]:
    # defaultdict, default values = set()
    artists: defaultdict = defaultdict(lambda: set())

    # artist_with_most_songs = None
    artist_with_most_songs = None

    # Loop over this dataset one line at a time
    with open(path, mode="r") as f:
        for line in csv.DictReader(f):
            # extract out the artist
            curr_artist: str = line["artist"]
            # extract out the song
            curr_song: str = line["song"]

            # if song in defaultdict[artist]
            if curr_song in artists[curr_artist]:
                continue
            else:
                # defaultdict[artist].add(song)
                artists[curr_artist].add(curr_song)

            if artist_with_most_songs is None or len(artists[curr_artist]) > len(
                artists[artist_with_most_songs]
            ):
                artist_with_most_songs = curr_artist

    # return artist_with_most_songs, defaultdict[artist]
    return artist_with_most_songs, artists[artist_with_most_songs]


if __name__ == "__main__":
    artist, songs = get_artists_with_most_songs(BB_PATH)
    print(f"Artist: {artist}\nSongs: {songs}")
