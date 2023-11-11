"""
Given an integer array nums, move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


Example 1:

Input: nums = [0,1,0,3,12]
             [1, 0, 0, 3]
             [1, 3, 0, 0, 12 ]
             [1, 3, 12, 0, 0]

Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]


edge1 : [1,2,3, 0, 0, 0]

edge2: [0, 0, 0, 1, 0, 2, 3]
"""
from typing import List


def move_zeros(array: List[int]) -> None:
    # Initialize a slow pointer
    slow: int = 0

    # Iterate over the array with a fast pointer
    for fast in range(len(array)):
        if array[slow] == 0 and array[fast] != 0:
            # Swap
            temp: int = array[fast]
            array[fast] = array[slow]
            array[slow] = temp

        # If slow isn't on a zero, incremement it up
        if array[slow] != 0:
            slow += 1


if __name__ == "__main__":
    array1: List[int] = [0, 1, 0, 3, 12]
    array2: List[int] = [0]
    array3: List[int] = [1, 2, 3, 0, 0, 0]
    array4: List[int] = [0, 0, 0, 1, 0, 2, 3]

    print(f"Original array: {array1}")
    move_zeros(array1)
    print(array1, "\n")

    print(f"Original array: {array2}")
    move_zeros(array2)
    print(array2, "\n")

    print(f"Original array: {array3}")
    move_zeros(array3)
    print(array3, "\n")

    print(f"Original array: {array4}")
    move_zeros(array4)
    print(array4, "\n")
