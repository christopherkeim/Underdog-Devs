"""
You are given an integer array input of length n. There are n vertical lines drawn 
such that the two endpoints of the ith line are (i, 0) and (i, input[i]).

Find two lines that together with the x-axis form a container, such that the container 
contains the most water.

Return the maximum amount of water a container can store.

Input: input = [1,8,6,2,5,4,8,3,7]
Output: 49

Input: input = [1,1]
Output: 1
"""
from typing import List


def calculate_area(heights: List[int]) -> int:
    # Initialize left pointer, right pointer, max area
    left: int = 0
    right: int = len(heights) - 1

    max_area: int = 0

    # Iterate until left and right pointers converge
    while left < right:
        curr_area: int = min(heights[left], heights[right]) * (right - left)
        max_area = max(max_area, curr_area)

        # If the value at left pointer < value at right pointer, incremenet left
        if heights[left] < heights[right]:
            left += 1
        # Otherwise decrement right (covers equivalent values)
        else:
            right -= 1

    return max_area


if __name__ == "__main__":
    test1: List[int] = [1, 0, 4, 0, 2, 1, 2, 6]
    test2: List[int] = [2, 1, 2, 0]
    print(calculate_area(test1))
    print(calculate_area(test2))
