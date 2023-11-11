"""
Write a function that takes as input two arguments:

1. An array of numbers
2. An integer `k`

and returns an array with all of the pairs of numbers from that array that sum 
to `k`. You can't use the same number twice. You can assume that there are no 
duplicate numbers in the array.

Example

- Input array: `[1, 9, 6, 3, 5, 4]`
- `k`: 10
- Result: `[[1, 9], [6, 4]]` // Note that `[5, 5]` is not in the solution
"""

from typing import List, Set, Dict

array: List[int] = [1, 9, 6, 3, 5, 4]


def get_pair_sum(array: List[int], k: int) -> List[int]:
    matches: List[List[int]] = []

    search_map: Set = set(array)

    # Loop over each index in this array - 1
    for i in range(len(array) - 1):
        search_map.remove(array[i])
        curr_search_term: int = k - array[i]

        if curr_search_term in search_map:
            matches.append([array[i], curr_search_term])

    return matches


def get_pair_sum_indices(array: List[int], k: int) -> List[int]:
    """
    Utilizes a dictionary for handling indices.

    Given an array of integers nums and an integer target, return indices of
    the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may
    not use the same element twice.

    You can return the answer in any order.
    """
    matches: List[int] = []
    # Holds each value and index in the array
    search_map: Dict[int, int] = {}

    # Loop over each index in this array
    for i in range(len(array)):
        curr_search_term: int = k - array[i]

        if curr_search_term in search_map:
            matches.append([search_map[curr_search_term], i])
        # Add this value and index to our search map
        search_map[array[i]] = i

    return matches


def pair_sum_set(array: List[int], k: int) -> List[int]:
    """
    Implements above algorithm when searching for only values.

    This shows that the above algorithm is generalized to hold both
    values and indices using a dictionary.
    """
    matches: List[int] = []
    search_map: Set[int] = set()

    for i in range(len(array)):
        # Calculate current search term
        curr_search_term: int = k - array[i]

        # If this search term is in our search map,
        # add the current value along with the search term to results
        if curr_search_term in search_map:
            matches.append([curr_search_term, array[i]])

        # Add this value to our search map
        search_map.add(array[i])

    return matches


if __name__ == "__main__":
    print(f"Test array: {array}")
    print("Returns the values of matches")
    print(get_pair_sum(array, k=10))
    print(get_pair_sum(array, k=9))
    print()

    # Tests for get_pair_sum_indices
    print("get_pair_sum_indices returns the indices of matches")
    res1: List[List[int]] = get_pair_sum_indices(array, k=10)
    res2: List[List[int]] = get_pair_sum_indices(array, k=9)

    print(res1)
    print(res2)

    assert array[res1[0][0]] == 1, "fail"
    assert array[res1[0][1]] == 9, "fail"
    assert array[res1[1][0]] == 6, "fail"
    assert array[res1[1][1]] == 4, "fail"

    assert array[res2[0][0]] == 6, "fail"
    assert array[res2[0][1]] == 3, "fail"
    assert array[res2[1][0]] == 5, "fail"
    assert array[res2[1][1]] == 4, "fail"

    # Tests for pair sum implementation with set
    print("\nTesting for set value only implementation.")
    print(pair_sum_set(array, k=10))
