"""
input: List[str] = [
    "0, 0, 1, 1, 1",
    "0, 1, 1, 0, 0",
    "0, 1, 1, 1, 1",
    "1, 1, 1, 1, 0",
]

Output: 3

input: List[str] = [
    "1, 0, 0, 1",
    "1, 0, 1, 0",
]

Output: 2

Contiguous 0's are hole - up, down, left, or right 

Count how many contiguous holes there are 
"""

from typing import List


# Iterative
def count_moats(input: List[str]) -> int:
    count: int = 0

    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == "0":
                # Count only the "top left corner" of a ship
                if (i == 0 or input[i - 1][j] == "1") and (
                    j == 0 or input[i][j - 1] == "1"
                ):
                    count += 1

    return count


if __name__ == "__main__":
    input_moats: List[str] = [
        "01111",
        "01100",
        "00111",
        "11110",
    ]

    input_moat2: List[str] = [
        "1001",
        "1010",
    ]
    print(count_moats(input_moats))
    print(count_moats(input_moat2))
