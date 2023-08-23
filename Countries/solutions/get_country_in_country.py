"""
Solution 6: There is at least one country name that contains another 
country name. Find all of these cases.
"""

import logging

logger: logging.RootLogger = logging.getLogger()


def get_country_in_country(data: list[str]) -> list[str]:
    """
    This function should consume the data in countries.txt and return the country
    names that are contained within other country names present in the dataset.
    """
