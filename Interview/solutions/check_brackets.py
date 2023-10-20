"""
Given a string of different bracket types (parentheses, square brackets, and curly 
braces), write a function that returns whether or not the string is balanced.

The string is balanced if each opening bracket is followed by a corresponding 
close bracket, and all brackets between those open and close brackets are also balanced.

Examples of balanced strings

- `{[()]}`
- `{}[]()`
- `[(){()}]`    

Examples of unbalanced strings

- `{[(])}` // Has a `]` before the `(` was closed with a `)`
- `{}][()` // Has a `]` without a preceding `[`
- `[(){()}` // Missing a closing `]`

For recursive implemention:
    Your base case is an empty string "" or a string with 1 bracket (open or close)
    "{"
"""
from typing import Dict, Set
from collections import deque


def check_brackets(sequence: str) -> bool:
    opening_brackets: Set[str] = {
        "(",
        "{",
        "[",
    }

    pairs: Dict[str, str] = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    q: deque = deque()

    # Loop over each character in the input string
    for letter in sequence:
        # Opening bracket
        if letter in opening_brackets:
            # enqueu opening bracket onto queue
            q.appendleft(letter)

        # Closing brace
        else:
            prev_opening_bracket: str = q.popleft()
            if pairs[letter] != prev_opening_bracket:
                return False

    if len(q):
        return False

    return True


if __name__ == "__main__":
    e1: str = "{[()]}"  # positive
    e2: str = "{[(])}"  # negative
    e3: str = "[(){()}"  # negative

    print(check_brackets(e1))
    print(check_brackets(e2))
    print(check_brackets(e3))
