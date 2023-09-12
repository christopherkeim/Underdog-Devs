"""
Solution 13: Write a function that takes a string phrase and 
returns a dictionary containing counts of how many times every 
character appears in phrase.
"""
# from collections import defaultdict, Counter


# Q1: Am I concerned about casing? --> all homogenous?

# Q2: Are all my inputs strings -> handle other objects

TEST_WORD1: str = "ABCDE"
TEST_WORD2: str = "AAABCDE"
TEST_WORD3: str = "AAABBCDE"
TEST_WORD4: str = "A B C D E "  # -> {" ":5}
TEST_WORD5: str = ""  # -> {}
TEST_WORD6: str = "abcde...."


def get_letter_counts_in_phrase(phrase: str) -> dict[str, int]:
    # Create an empty dictionary for counts
    counts_dict: dict[str, int] = {}
    # Loop through each character in the phrase
    for char in phrase:
        # If not in dict, add key = 1
        if char not in counts_dict:
            counts_dict[char] = 1
        else:
            # If already in dict, key += 1
            counts_dict[char] += 1

    return counts_dict


if __name__ == "__main__":
    result1: dict[str] = get_letter_counts_in_phrase(TEST_WORD1)
    assert result1 == {"A": 1, "B": 1, "C": 1, "D": 1, "E": 1}, "FAIL"

    result2: dict[str] = get_letter_counts_in_phrase(TEST_WORD2)
    assert result2 == {"A": 3, "B": 1, "C": 1, "D": 1, "E": 1}, "FAIL"

    result3: dict[str] = get_letter_counts_in_phrase(TEST_WORD3)
    assert result3 == {"A": 3, "B": 2, "C": 1, "D": 1, "E": 1}, "FAIL"

    result4: dict[str] = get_letter_counts_in_phrase(TEST_WORD4)
    assert result4 == {"A": 1, "B": 1, "C": 1, "D": 1, "E": 1, " ": 5}, "FAIL"

    result5: dict[str] = get_letter_counts_in_phrase(TEST_WORD5)
    assert result5 == {}, "FAIL"

    result6: dict[str] = get_letter_counts_in_phrase(TEST_WORD6)
    assert result6 == {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1, ".": 4}, "FAIL"

    print("SUCCESS!!!!!!!!!!!!!!!!!!!!!!")
