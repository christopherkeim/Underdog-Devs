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

from typing import List, Set

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


if __name__ == "__main__":
    print(get_pair_sum(array, k=10))
    print(get_pair_sum(array, k=9))
