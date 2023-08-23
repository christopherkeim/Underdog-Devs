"""
Solution 1: What are all of the countries that have “United” in the name?
"""
import logging

logger = logging.getLogger()


def get_united(data: list[str]) -> list[str]:
    """
    This function should consume the countries.txt data and return all of the words that
    containing "United".
    """

    # Check if we have the correct parameter input type
    logger.info("Checking data type of input.")
    if not isinstance(data, list) or not all(isinstance(word, str) for word in data):
        raise TypeError("This function requires a list of strings as input.")

    # Initialize an empty list
    united_words: list[str] = []

    # Loop through each word in our data
    logger.info("Extracting countries with 'United' in them.")

    for word in data:
        # Check if the word contains 'United'
        if "United" in word:
            united_words.append(word)

    return united_words
