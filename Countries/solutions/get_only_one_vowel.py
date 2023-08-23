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
