"""
Solution 11: Write a function that takes a string word as an argument 
and returns a count of all of the “A”s in that string.
"""

TEST_1: str = "XXXAAAXX"
TEST_2: str = "XA"
TEST_3: str = "XXXXX"
TEST_4: str = "AAAA"


def count_all_a_in_word(word: str) -> int:
    count: int = 0
    for i in range(len(word)):
        if word[i] == "A":
            count += 1
    return count


if __name__ == "__main__":
    print(count_all_a_in_word(TEST_1))
    print(count_all_a_in_word(TEST_2))
    print(count_all_a_in_word(TEST_3))
    print(count_all_a_in_word(TEST_4))
