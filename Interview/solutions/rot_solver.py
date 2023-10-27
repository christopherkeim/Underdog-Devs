"""
Write a function `rot` that:

- takes as arguments: an input string and an amount by which to shift the letters 
in the string
- returns: the input string, shifted by the shift amount

The function should preserve case — it should be able to handle both upper and 
lowercase letters — and it should not alter punctuation. The function should 
support negative numbers. The function should support large shift numbers.

Sample inputs and outputs:


    rot("HELLO", 1) -> "IFMMP" # shift right by 1
    rot("HELLO", 2) -> "JGNNQ" # shift right by 2
    rot("HELLO", -1) -> "GDKKN" # shift left by 1
    rot("HELLO", 27) -> "IFMMP" # shift right by 27, wrapping back to the beginning
    rot("Hello, Rick", 1) -> "Ifmmp, Sjdl" # Preserve case and punctuation
    rot(rot("Hello, Rick", 1), -1) -> "Hello, Rick"

Writing this function will require familiarity with converting between character 
and ordinals. For example, Python has the `ord` and `chr` functions, and JavaScript 
has the `charCodeAt` and `fromCharCode` String methods.

You may also find reviewing modular arithmetic (using `%`) to be helpful.


Part II

Using your `rot` function, write a function `decrypt` that takes a text encrypted 
using a shift substitution cipher of an unknown shift amount, and returns a tuple 
containing ` the shift used to encrypt the original string, the original string)`.

You will need a dictionary or word list. An input string needs to be long enough 
to unambiguously determine the the shift used, or there could be multiple valid 
shifts.

Sample inputs and outputs:

```
decrypt("Ju xbt uif cftu pg ujnft, ju xbt uif xpstu pg ujnft") -> 
    ("It was the best of times, it was the worst of times", 1)
```
"""
from typing import List, Set, Tuple
from pathlib import Path
import re


def rot_solver(input: str, offset: int) -> str:
    if len(input) == 0:
        return ""

    if not isinstance(offset, int):
        raise TypeError("Offset must be of type int.")

    LOWERCASE_FLOOR: int = ord("a")
    UPPERCASE_FLOOR: int = ord("A")

    result: List[str] = []

    # Iterate over each character in this string
    for letter in input:
        # Uppercase letters
        if letter.isupper():
            normalized_upper: int = ord(letter) - UPPERCASE_FLOOR
            wrapped_ord: int = (normalized_upper + offset) % 26
            new_char: str = chr(wrapped_ord + UPPERCASE_FLOOR)
            result.append(new_char)

        # Lowercase letters
        elif letter.islower():
            normalized_lower: int = ord(letter) - LOWERCASE_FLOOR
            wrapped_ord: int = (normalized_lower + offset) % 26
            new_char: str = chr(wrapped_ord + LOWERCASE_FLOOR)
            result.append(new_char)

        # Punctuation
        else:
            result.append(letter)

    # Tranforms the dynamic array -> string
    return "".join(result)


def decrypt(input: str) -> Tuple[str, int]:
    """
    Example:

    decrypt("Ju xbt uif cftu pg ujnft, ju xbt uif xpstu pg ujnft") ->
        ("It was the best of times, it was the worst of times", 1)


    # range(1, -1, 2, -2, 3, -3)
    # for i in range(1, 101):
    #    range.append(i)
    #    range.append(-i)
    """

    WORDS: Set[str] = load_words_from_file()

    # Loop over range of offset values
    for i in range(-50, 51):
        # Get candidate string
        candidate: List[str] = rot_solver(input, i)
        # Lower, remove punctuation, then split the string on spaces
        substrings: List[str] = re.sub(r"[^\w\s]", "", candidate.lower()).split()

        if all(ss in WORDS for ss in substrings):
            # Because we're doing an inverse operation to decrypt the string,
            # return the inverse offset
            return (candidate, -i)

    return ("None found", 0)


def load_words_from_file() -> Set[str]:
    """
    Returns a set containing all words found in sowpods.txt.

    Note that "A" is not in this dataset.
    """
    SCRABBLE_PATH: Path = Path("Interview/tests/fixtures/sowpods.txt")
    words: Set[str] = set()

    with open(SCRABBLE_PATH, mode="r") as f:
        for line in f:
            words.add(line.strip().lower())

    words.add("a")

    return words


if __name__ == "__main__":
    # Rot Solver testing
    print(rot_solver("HELLO", 50))
    print(rot_solver("HELLO", 2))
    print(rot_solver("HELLO", -1))
    print(rot_solver("HELLO", 27))
    print(rot_solver("Hello, Rick", 1), "\n")

    # Decrypt testing
    test_string: str = rot_solver(
        "It's a glorious wonderful day, the cat jumped off the sofa", 48
    )
    print(test_string)

    result: Tuple[str, int] = decrypt(test_string)
    print(result)

    assert result == (
        "It's a glorious wonderful day, the cat jumped off the sofa",
        48,
    ), "FAILURE"

    print("Good job.")
