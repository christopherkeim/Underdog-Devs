"""
Solution 2: What countries both begin and end with a vowel?
"""
import logging

logger = logging.getLogger()


def get_begin_end_vowel(data: list[str]) -> list[str]:
    """
    This function should consume the data in countries.txt and return
    a list of the countries that start and end with vowels.
    """

    # Check if we have the correct parameter input type
    logger.info("Checking data type of input.")
    if not isinstance(data, list) or not isinstance(data[0], str):
        raise TypeError("This function requires a list of strings as input.")

    # Initialize a list of vowels
    vowels: list[str] = ["a", "e", "i", "o", "u"]

    # Initialize an empty list
    vowel_countries: list[str] = []

    # Loop through each word in our data
    logger.info("Extracting countries with vowels at front and end.")

    for word in data:
        # Check if this word begins and ends with a vowel
        word_len = len(word)
        if word[0].lower() in vowels and word[word_len - 1].lower() in vowels:
            vowel_countries.append(word)

    # Return our list of countries
    return vowel_countries
