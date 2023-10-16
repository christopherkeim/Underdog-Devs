"""
Postnotation Calculator 

Most of us learn how to do math with operators in between numbers. For example:

`(((4 * 3) + 1) - 2) = 11`

You have an operator like `+ - * /`, and numbers (“operands”) on each side of the 
operator, and you apply the operator to those operands. If you have multiple 
expressions, you resolve them according to some order of operations (or forcing 
the order using parenthesis). This way of doing math uses infix notation — the 
operators are in between the operands.

There's another way of doing math that uses postfix notation — the operators come 
after the operands. This is a cool way of doing math — you don't need parenthesis or 
rules to describe the order of operations, so it's easier to parse a math expression, 
and you can use a stack to manage the calculation (using the stack data structure in 
the real world!).

Let's build a basic postfix notation calculator.

What to implement

Write a function that takes as an argument a string containing a mathematical 
expression in postfix notation, using as available operators `+ - * /`. The function
should return the result of evaluating that expression.


Example string: "1 3 4 * + 2 -" -> 11
"""

# Number: if you see a number you push it onto the stack

# Operator (* + / ...): Pop the last 2 operands off the stack, apply the operator,
# and push the result back onto the stack
from typing import Union, Callable, Dict, List
from collections import deque


# -> 11
TEST_1: str = "1 3 4 * + 2 -"

# -> 3
TEST_2: str = "3 2 1 + + 2 /"

# -> error
TEST_3: str = "2 +"

# float -> 2.72
TEST_4: str = "3 2 1 + + 2.2 /"


def postfix_notation_calculator(input: str) -> Union[int, float]:
    """
    Postfix notation calculator that parses an input string and returns its
    mathematical result.
    """
    OPERATORS: Dict[str, Callable] = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    # Instantiate a stack
    stack: deque = deque()

    # Get rid of spaces
    input: List[str] = input.split()

    # Input string must contain at least 2 numbers and an operator
    if len(input) <= 2:
        raise ValueError("Invalid input.")

    # Loop over each character in the string
    for char in input:
        # Integer character
        if char.isdigit():
            # push it to stack
            stack.append(int(char))
        # Float character
        elif char.replace(".", "").isdigit():
            stack.append(float(char))

        # Operator character
        else:
            # Error handling for invalid operator
            if char not in OPERATORS:
                raise ValueError("Invalid operator.")

            # Error handling for more operators than numbers
            if len(stack) < 2:
                raise ValueError("More operators than numbers.")

            # Pop the last 2 numbers off the stack
            number2: Union[int, float] = stack.pop()
            number1: Union[int, float] = stack.pop()
            # Apply this operator character to both numbers
            result: Union[int, float] = OPERATORS[char](number1, number2)

            if (
                number1 > number2
                and isinstance(number2, int)
                and isinstance(number1, int)
            ):
                result = int(result)

            # push the resultant number onto stack
            stack.append(result)

    if len(stack) > 1:
        raise ValueError("Invalid input, not enough operators.")

    # return the result -> pop the last number from the stack and return
    resultant_number: Union[int, float] = stack.pop()
    return resultant_number


if __name__ == "__main__":
    print(postfix_notation_calculator(TEST_4))
