"""
Solution 12: Write a function that takes a string word as 
the first argument, a string letter as the second argument,
and returns a count of how many times letter occurs in word.

"""

TEST_LETTER: str = "A"

TEST_WORD1: str = "ALFALFA"
TEST_WORD2: str = "AXXXXXX"
TEST_WORD3: str = "XXXXXXX"
TEST_WORD4: str = ""


def get_letter_count_in_word(word: str, letter: str) -> int:
    # Initialize a counter = 0
    counter: int = 0

    # Loop over each letter in the word
    for i in range(len(word)):
        if word[i] == "A":
            counter += 1

    return counter


if __name__ == "__main__":
    print(get_letter_count_in_word(TEST_WORD1, TEST_LETTER))
    print(get_letter_count_in_word(TEST_WORD2, TEST_LETTER))
    print(get_letter_count_in_word(TEST_WORD3, TEST_LETTER))
    print(get_letter_count_in_word(TEST_WORD4, TEST_LETTER))
