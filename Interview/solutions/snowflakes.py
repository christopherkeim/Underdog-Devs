"""
We're given a collection of snowflakes, and we have to determine whether any 
of the snowflakes in the collection are identical.

A snowflake is represented by six integers, where each integer gives the length of 
one of the snowflake's arms. For example, this is a snowflake:
3, 9, 15, 2, 1, 10

Snowflakes can also have repeated integers, such as
8, 4, 8, 9, 2, 8


Examples of wrapping + different direction movement:

1, 2, 3, 4, 5, 6

and

3, 2, 1, 6, 5, 4

NOTE:

Conceptually this is a ring buffer (itertools cycle)
"""

from typing import List
from collections import defaultdict


def are_identical(sf1: List[int], sf2: List[int]) -> bool:
    for i in range(len(sf2)):
        if compare_right(sf1, sf2, i):
            return True

        if compare_left(sf1, sf2, i):
            return True

    return False


def compare_right(sf1: List[int], sf2: List[int], sf2_start_idx: int) -> bool:
    for i in range(len(sf1)):
        if sf1[i] != sf2[(sf2_start_idx + i) % len(sf2)]:
            return False

    return True


def compare_left(sf1: List[int], sf2: List[int], sf2_start_idx: int) -> bool:
    for i in range(len(sf1)):
        if sf1[i] != sf2[(sf2_start_idx - i) % len(sf2)]:
            return False

    return True


def group_by_sums(snowflakes: List[List[int]]) -> defaultdict[int, List[List[int]]]:
    """
    Max amount of snowflakes: 100_000
    """
    # Initialize storage for our resultant groups
    grouped_snowflakes: defaultdict[int, List[List[int]]] = defaultdict(list)

    # Iterate over the list of snowflakes
    for snowflake in snowflakes:
        # Sum their element values
        value_sum: int = sum(snowflake) % 100_000

        # Append snowflake as entry to storage at key of sum
        grouped_snowflakes[value_sum].append(snowflake)

    # return out grouped snowflakes for downstream processing
    return grouped_snowflakes


"""
1. Is there a way to early return
2. Is there a way to group snowflakes together for comparison
    - if sum(sf1) != sum(sf2) they are not worth iteratively comparing
"""


if __name__ == "__main__":
    snowflake1: List[int] = [1, 2, 3, 4, 5, 6]
    snowflake2: List[int] = [3, 2, 1, 6, 5, 4]
    snowflake3: List[int] = [3, 9, 15, 2, 1, 10]
    snowflake4: List[int] = [1, 2, 3, 4, 5, 6]
    snowflake5: List[int] = [4, 5, 6, 1, 2, 3]

    print(are_identical(snowflake1, snowflake2))
    print(are_identical(snowflake1, snowflake3))
    print(are_identical(snowflake4, snowflake5))

    assert are_identical(snowflake1, snowflake2), "FAILURE"
    assert not are_identical(snowflake1, snowflake3), "F"
    assert are_identical(snowflake4, snowflake5), "F"
