"""
Solution 1: What movies on this list were distributed by DreamWorks?
"""

import csv
import logging

logging.basicConfig(level=logging.INFO)
logger: logging.RootLogger = logging.getLogger()


def get_dreamworks_movies() -> set:
    """
    This function should consume a csv file holding the top 1000 grossing movies
    with the columns 'Title', 'Distributor', 'Release Date', 'US Sales',
    'World Sales', 'Runtime', 'Rating', and return a set with the movies
    distributed by DreamWorks.
    """

    # Initialize a set to hold our DreamWorks movies
    dreamworks_movies: set = set()

    # Read the csv file into a matrix
    logger.info("Loading top_movies.csv into memory.")

    with open("Movies/tests/fixtures/top_movies.csv", mode="r") as csv_file:
        reader: list[list[str]] = csv.reader(csv_file)

        # Loop through each row in this matrix
        logger.info("Extracting movies distributed by DreamWorks.")
        for row in reader:
            # Extract the Distributor of the movie
            dist: str = row[1]

            # Extract the Name of the movie
            name: str = row[0]

            # If the Distributor contains "dreamworks", add it to our set of movies
            if "dreamworks" in dist.lower():
                dreamworks_movies.add(name)

    # Return the movies distributed by DreamWorks
    return dreamworks_movies


# Main
if __name__ == "__main__":
    result: set = get_dreamworks_movies()
    length: int = len(result)
    logger.info(result)
    logger.info(f"Length of results: {length}")
