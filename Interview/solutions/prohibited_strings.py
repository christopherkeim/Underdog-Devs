"""
Write a function that takes two arguments, a list of prohibited strings 
and a username, and returns a boolean of whether or not the username contains
any of the prohibited strings.

Some important details:

- The list of prohibited words will provide words in some casing, and we want 
to be case-insensitive in our checks. For example, if “darn” is a prohibited word, 
“darn”, “DARN” and “DaRn” are all prohibited.

- Sometimes people like to make usernames that substitute numbers for letters, 
to try to get around a prohibited word list. We also want to make those substitutions 
prohibited. The specific letter substitutions we need to check are:
    - A becomes 4
    - E becomes 3
    - I becomes 1
    - O becomes 0
    - For example, if “darn” is a prohibited word, “d4rn” is also a prohibited word. 
    If “darn” and “heck” are prohibited words, the username “D4RN_y0u_T0_h3ck” contains 
    prohibited words.
"""

# Examples: "darn", "heck", "D4RN_y0u_T0_h3ck"

from typing import List, Set, Dict

TEST_USER: str = "D4RN_y0u_To_h3ck"
TEST_PROB_STRS: List[str] = ["darn", "heck"]

# Assumption 1: all valid ascii characters are permissible in username

# Note: to handle casing, cast all to lowercase before checks


def is_prohibited_string(prob_strings: List[str], username: str) -> bool:
    # Define mapping for letter -> numerical string
    LETTER_SUBSTITUTIONS: Dict[str, str] = {
        "4": "a",
        "3": "e",
        "1": "i",
        "0": "o",
    }

    # lowercase the username
    username: str = username.lower()
    # Convert string without subs for check
    for sub in LETTER_SUBSTITUTIONS:
        if sub in username:
            username = username.replace(sub, LETTER_SUBSTITUTIONS[sub])

    # Cast prob_strings to set for efficient checks
    prob_strings: Set[str] = set(word.lower() for word in prob_strings)

    # Loop over prob_strings and check if they are present in username
    for prob_word in prob_strings:
        if prob_word in username:
            return True

    return False


if __name__ == "__main__":
    print(is_prohibited_string(TEST_PROB_STRS, TEST_USER))
