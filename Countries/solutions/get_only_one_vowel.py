"""
Solution 5: What countries use only one vowel in their name 
(the vowel can be used multiple times)? 
"""

import logging

logger: logging.RootLogger = logging.getLogger()


def get_only_one_vowel(data: list[str]) -> list[str]:
    """
    This function should consume the data in countries.txt and return a list of
    the countries that contain only one vowel in their name.
    """

    # Check that we have the correct parameter input data type
    if not isinstance(data, list) or not all(isinstance(word, str) for word in data):
        raise TypeError("This function requires a list of strings as input.")

    # Initialize a list to hold countries with only one vowel
    one_vowel: list[str] = []

    # Define vowels set
    vowels: set = {"a", "e", "i", "o", "u"}

    # Loop through each country in our dataset
    logger.info("Extracting countries containing only one vowel.")
    for country in data:
        # Initialize an empty set to hold vowel sampling
        vowel_count: set = set()

        # Loop through each letter in this country
        for letter in country:
            # Check if that letter is in vowels, if so add it to intra-country vowel set
            if letter.lower() in vowels:
                vowel_count.add(letter.lower())

        # Check if the country has exactly 1 vowel
        if len(vowel_count) == 1:
            one_vowel.append(country)

    # Return the list of countrys with only 1 vowel
    return one_vowel
