"""
Solution 1: What movies on this list were distributed by DreamWorks?
"""

import csv


def get_dreamworks_movies() -> set:
    """
    This function should consume a matrix holding the top movies
    with the columns 'Title', 'Distributor', 'Release Date', 'US Sales',
    'World Sales', 'Runtime', 'Rating', returning a set with the movies
    distributed by DreamWorks.
    """

    # Initialize a set to hold our DreamWorks movies
    dreamworks_movies: set = set()

    # Read my csv file into object
    with open("Movies/tests/fixtures/top_movies.csv", mode="r") as c:
        reader: csv.reader = csv.reader(c)
        for row in reader:
            # Extract the Distributor of the movie
            dist = row[1]
            # Extract the Name of the movie
            name = row[0]
            # If the Distributor contains "dreamworks", add it to our set of movies
            if "dreamworks" in dist.lower():
                dreamworks_movies.add(name)

    # Return the movies distributed by DreamWorks
    return dreamworks_movies


# Main
if __name__ == "__main__":
    result = get_dreamworks_movies()
    length = len(result)
    print(result)
    print(f"Length of results: {length}")
