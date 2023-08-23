"""
Solution 6: There is at least one country name that contains another 
country name. Find all of these cases.
"""

import logging

logger: logging.RootLogger = logging.getLogger()


def get_country_in_country(data: list[str]) -> set:
    """
    This function should consume the data in countries.txt and return the country
    names that are contained within other country names present in the dataset.
    """

    # Check that we have the correct parameter input data type
    if not isinstance(data, list) or not all(
        isinstance(country, str) for country in data
    ):
        raise TypeError("This function requires a list of strings as input.")

    # Initialize a set for storing discovered countries
    c_in_c: set = set()

    # Loop through each country in the dataset
    logger.info("Discovering countries that appear within other countries.")
    for i, country in enumerate(data):
        # If the current index is 0, slice it out of our search array
        if i == 0:
            search_array: list[str] = data[i + 1 :]
        # If the current index is last, slice it out of our search array
        elif i == (len(data) - 1):
            search_array: list[str] = data[0:i]
        # For each index other than first or last, slice it out of our search array
        else:
            search_array: list[str] = data[0:i] + data[i + 1 :]

        # Check if our current country is contained within any other country
        for s_country in search_array:
            if country.lower() in s_country.lower():
                c_in_c.add(country)

    # Return our list of countries in countries
    return c_in_c
