"""
Given an integer array nums, return an array answer such that answer[i] is equal 
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 
32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division 
operation.

Example 1:

Input: nums = [1,2,3,4]

Output: [24,12,8,6]

"""
from typing import List


def product_of_array_except_self(input: List[int]) -> List[int]:
    # Initialize postfix, prefix, output array -> value 1
    prefix: int = 1
    postfix: int = 1

    length: int = len(input)
    out: List[int] = [1] * length

    # Loop 1: iterates forward AND backward through our input array
    for i in range(length):
        # Multiply prefix value into out[i]
        out[i] *= prefix
        # update prefix as prefix *= input[i]
        prefix *= input[i]

        # Multiply postfix value into out[length - 1 - i]
        out[length - 1 - i] *= postfix
        # update postfix as postfix *= input[length - 1 - i]
        postfix *= input[length - 1 - i]

    return out


if __name__ == "__main__":
    EXAMPLE1: List[int] = [1, 2, 3, 4]  # [24,12,8,6]
    EXAMPLE2: List[int] = [-1, 2, 3, 4]  # [24,-12,-8,-6]
    EXAMPLE3: List[int] = [10, -2, 5, -10]  # [100, -500, 200, -100]
    EXAMPLE4: List[int] = [9, 6, 0, 2]  # [0, 0, 108, 0]

    print(product_of_array_except_self(EXAMPLE1))
    print(product_of_array_except_self(EXAMPLE2))
    print(product_of_array_except_self(EXAMPLE3))
    print(product_of_array_except_self(EXAMPLE4))
