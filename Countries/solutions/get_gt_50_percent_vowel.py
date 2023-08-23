"""
Solution 3: What country names are > 50% vowels?
"""
import logging

logger = logging.getLogger()


def get_gt_50_percent_vowel(data: list[str]) -> list[str]:
    """
    This function will consume the data in countries.txt and return a list of
    countries that contain > 50% vowels.
    """

    # Check if we have the correct paramter input type
    logger.info("Checking data type of input.")
    if not isinstance(data, list) or not all(isinstance(word, str) for word in data):
        raise TypeError("This function requires a list of strings as input.")

    # define our vowels in list[str]
    vowels: list[str] = ["a", "e", "i", "o", "u"]

    # Initialize a list for our vowel_words
    gt_50_vowels: list[str] = []

    # Loop through each word in data
    for word in data:
        # Initialize a counter
        counter: int = 0
        # Store the total length of the word
        word_length: int = len(word)
        # Loop over each character in the word and increment vowel counts
        for letter in word:
            # If the letter is a vowel += counter
            if letter.lower() in vowels:
                counter += 1
        # If the word is composed of > 50% vowels append it to gt_50_vowels list
        if (counter / word_length) > 0.5:
            gt_50_vowels.append(word)

    # return our list of vowel words
    return gt_50_vowels
