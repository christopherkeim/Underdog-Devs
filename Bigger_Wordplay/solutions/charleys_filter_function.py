"""
Requirements:

    1. Read the dataset into memory and operate on it like a list

    2. Pass "predicate functions" (boolean functions) to your function 
       as parameters 
       - They accept something and return true/false and are 
         great for filter determinations

    3. Use a timing function as well
"""

from typing import List, Set, Callable
from pathlib import Path
import time


SCRABBLE_PATH: Path = Path("Bigger_Wordplay/tests/fixtures/sowpods.txt")


def timeit(fn: Callable) -> None:
    """
    A decorator for timing the execution of functions.
    """

    def get_time(*args, **kwargs) -> None:
        """
        *args and **kwargs support positional and kw arguments of fn
        """
        start_time: float = time.time()
        # Call the function and store its output
        fn_output = fn(*args, **kwargs)
        # Print time taken for function execution to std
        print(f"Time taken in {fn.__name__}: {time.time() - start_time} seconds\n")
        # Decorator returns output of function
        return fn_output

    # Return the get_time function object
    return get_time


@timeit
def load_data_from_text_file(path: Path) -> List[str]:
    with open(path, mode="r") as f:
        data: List[str] = f.read().splitlines()
    return data


def is_ge_8_chars(word: str) -> bool:
    """
    Predicate function measuring the condition that a word is composed
    of 8 characters or more.
    """
    if len(word) < 8:
        return False

    return True


def is_le_3_unique_chars(word: str) -> bool:
    """
    Predicate function measuring the condition that a word is composed
    of 3 or fewer unique letters.
    """
    if len(set(word)) > 3:
        return False

    return True


@timeit
def filter_words(
    words: List[str], predicate1: Callable, predicate2: Callable
) -> List[str]:
    """
    Takes a list of strings and two passed in predicate functions and filters
    this list using the predicate functions.

    Predicate functions should be passed in order of "least expensive" to
    "most expensive" and will be applied in this order.
    """
    matches: List[str] = []

    for word in words:
        if not predicate1(word):
            continue

        if predicate2(word):
            matches.append(word)

    return matches


if __name__ == "__main__":
    data = load_data_from_text_file(SCRABBLE_PATH)

    # Case 1: is_ge_8_chars as first predicate condition
    print("Case 1: Using is_ge_8_chars() as 1st predicate:\n")
    matches1: List[str] = filter_words(
        data, predicate1=is_ge_8_chars, predicate2=is_le_3_unique_chars
    )
    print(matches1, "\n")

    # Case 2: is_le_3_unique_chars as first predicate condition
    print("Case 2: Using is_le_3_unique_chars() as 1st predicate:\n")
    matches2: List[str] = filter_words(
        data, predicate1=is_le_3_unique_chars, predicate2=is_ge_8_chars
    )
    print(matches2)
