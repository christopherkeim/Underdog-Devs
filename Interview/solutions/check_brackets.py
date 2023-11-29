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
from typing import Dict, Set, List, Optional
from collections import deque


def check_brackets(sequence: str) -> bool:
    # Odd length strings are always unbalanced
    if len(sequence) % 2 != 0:
        return False

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

    stack: deque = deque()

    # Loop over each character in the input string
    for letter in sequence:
        # Opening bracket
        if letter in opening_brackets:
            # Push opening bracket onto stack
            stack.append(letter)

        # Closing bracket
        else:
            if len(stack) == 0:
                return False
            # Pop prev opening bracket from stack
            prev_opening_bracket: str = stack.pop()
            if pairs[letter] != prev_opening_bracket:
                return False

    if len(stack) > 0:
        return False

    return True


def check_brackets_recursive(sequence: str, opens: Optional[List[str]] = None) -> bool:
    # Initialize opens array on first call
    opens: List[str] = opens or []
    # Base cases
    if sequence == "":
        return True

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

    if sequence[0] in opening_brackets:
        opens += [sequence[0]]
        return check_brackets_recursive(sequence[1:], opens)

    if len(opens) == 0:
        return False

    return (
        pairs[sequence[0]] == opens.pop()
        and check_brackets_recursive(sequence[1:], opens)
        and len(opens) == 0
    )


if __name__ == "__main__":
    e1: str = "{[()]}"  # positive
    e2: str = "{[(])}"  # negative
    e3: str = "[(){()}"  # negative
    e4: str = ")"
    e5: str = "{[]}"
    e6: str = ""
    e7: str = "{[{(){}}]({})()}"
    e8: str = "{[{(){}}]({})()}]"

    print(check_brackets(e1))
    print(check_brackets(e2))
    print(check_brackets(e3))
    print(check_brackets(e4))

    print(check_brackets_recursive(e1))
    print(check_brackets_recursive(e2))
    print(check_brackets_recursive(e3))
    print(check_brackets_recursive(e4))
    print(check_brackets_recursive(e5))
    print(check_brackets_recursive(e6))
    print(check_brackets_recursive(e7))
    print(check_brackets_recursive(e8))
