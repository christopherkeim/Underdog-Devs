"""
Solution 1: 

Print out all of the #1 songs and the artists who made them. If a song was #1 
for more than one week, only print it once. Example output:

    These were the number one songs of 2000:
    "Try Again" - Aaliyah
    "Say My Name" - Destiny's Child
    "What A Girl Wants" - Christina Aguilera
    "Maria Maria" - Santana Featuring The Product G&B
    "Smooth" - Santana Featuring Rob Thomas
    "Independent Women Part I" - Destiny's Child
"""

# Q1: A song + artist is defined as number 1 if its rank == 1

# Q2: Is this dataset static and valid?

from typing import Tuple, Set
from pathlib import Path
import csv

BB_PATH: Path = Path("Billboard/tests/fixtures/billboard100_2000.csv")


def print_number_1_songs_and_artists(path: Path) -> None:
    matches: Set = set()

    # Load this csv file into memory - line by line
    with open(path, mode="r") as f:
        for line in csv.DictReader(f):
            # Extract rank value
            curr_rank: str = line["rank"]
            # Guard clause
            if curr_rank != "1":
                continue

            # Extract out the song and artist
            match_tuple: Tuple[str, str] = (line["song"], line["artist"])

            if match_tuple in matches:
                continue

            # Store them as a tuple within a set
            matches.add(match_tuple)

    # Print Number one songs of 2000
    print("Number one songs of 2000: \n")
    for song, artist in matches:
        print(f'"{song}" - {artist}')


if __name__ == "__main__":
    print_number_1_songs_and_artists(BB_PATH)
