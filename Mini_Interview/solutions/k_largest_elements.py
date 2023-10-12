"""
Write a function that takes as input two arguments:

1. An array of numbers
2. An integer `k`

and returns the `k` largest values from that array. The order of the elements in 
the returned array doesn't matter.

Example

- Input array: `[5, 16, 7, 9, -1, 4, 3, 11, 2]`
- `k`: 3
- Result: `[16, 9, 11]`

"""
from typing import List
import heapq
from queue import PriorityQueue

a: List[int] = [5, 16, 7, 9, -1, 4, 3, 11, 2]


def get_k_largest_elements_brute_force(arr: List[int], k: int) -> List[int]:
    """
    Time complexity: O(n ln(n))
    """
    sorted_list: List[int] = sorted(arr, reverse=True)
    return sorted_list[0:k]


def get_k_largest_elements_priority_queue(arr: List[int], k: int) -> List[int]:
    """
    Insertion: O(n ln(n)) to populate the priority queue -> theta ln(n)

    Get: O(1) to retrieve them one at a time -> everytime you pop an element off
    the top you need to restructure your tree again
    """
    results: List[int] = heapq.nlargest(k, arr)
    return results


def get_k_largest_elements_small_min_heap(arr: List[int], k: int) -> List[int]:
    # use min heap
    heap = PriorityQueue(maxsize=k + 1)
    # loop over each integer
    for number in arr:
        # add the number to the heap
        heap.put(number)

        if heap.qsize() > k:
            heap.get()

    return heap.queue


if __name__ == "__main__":
    print(get_k_largest_elements_brute_force(a, k=3))
    print(get_k_largest_elements_priority_queue(k=3, arr=a))
    print(get_k_largest_elements_small_min_heap(k=3, arr=a))
