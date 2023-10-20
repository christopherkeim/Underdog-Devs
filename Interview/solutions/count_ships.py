"""
Write a function that counts of the number of ships in a 2D grid.

- Input: an array of arrays of strings, representing a 2D grid. The strings are 
  either a `"."` for open water, or an `"S"` for part of a ship. Connected `"S"`es 
  are part of the same ship.
- Output: an integer that is the count of the number of ships in the grid.

Facts about ships:

- Ships are only horizontal or vertical, not diagonal.
- Ships have a width of one or more and a height of one or more.
- Ships never touch each other.

The input will always be a well-formed grid (all rows are the same length).

EXAMPLE 1
```
let ships = [
    [".", "S", ".", "S"],
    [".", ".", ".", "S"],
    ["S", "S", ".", "S"],
    [".", ".", ".", "S"],
]
countShips(ships) -> 3
```

EXAMPLE 2
```
let ships = [
    ["S", "S", ".", "S", "S", "S", ".", "."],
    ["S", "S", ".", "S", "S", "S", ".", "."],
    ["S", "S", ".", ".", ".", ".", "S", "S"],
]
countShips(ships) -> 3
```

NOTE: Implement this as DFS with a Graph.
"""
from typing import List


EXAMPLE1: List[List[str]] = [
    [".", "S", ".", "S"],
    [".", ".", ".", "S"],
    ["S", "S", ".", "S"],
    [".", ".", ".", "S"],
]

EXAMPLE2: List[List[str]] = [
    ["S", "S", ".", "S", "S", "S", ".", "."],
    ["S", "S", ".", "S", "S", "S", ".", "."],
    ["S", "S", ".", ".", ".", ".", "S", "S"],
]

EXAMPLE3: List[List[str]] = [
    [".", ".", ".", ".", "."],
    ["S", "S", "S", ".", "."],
    ["S", "S", "S", ".", "S"],
    ["S", "S", "S", ".", "."],
]


def count_ships(ships: List[List[str]]) -> int:
    """
    1. A ship is present if it is separated from other ships by negative space (".").
      - these can be considered termination signals

    2. A ship is constituted of 1 or more "corners", which are "S" values surrounded by
    atleast 2 "." values (horizontal and vertical indices only).
      - an "edge" of the matrix counts as a "corner" here, meaning that "." ==
        i=0, len(ships) and "." == j=0, len(row).


    Here we will count a ship once if and only if we discover it has a top left corner
    consisting of:

    [      "." ] <- vertical negative space = [i - 1][j]
    [ ".", "S" ] <- horizontal negative space = [i][j - 1]

    """
    # Storage for count
    count: int = 0

    for i, row in enumerate(ships):
        for j, cell in enumerate(row):
            if ships[i][j] == "S":
                # Count only the "top left corner" of a ship
                if (i == 0 or ships[i - 1][j] == ".") and (
                    j == 0 or ships[i][j - 1] == "."
                ):
                    count += 1

    return count


if __name__ == "__main__":
    e1: int = count_ships(EXAMPLE1)
    e2: int = count_ships(EXAMPLE2)
    e3: int = count_ships(EXAMPLE3)

    print(f"EXAMPLE1 number of ships: {e1}")
    print(f"EXAMPLE2 number of ships: {e2}")
    print(f"EXAMPLE2 number of ships: {e3}")
