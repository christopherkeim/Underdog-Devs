"""
Boggle solver.
"""
from typing import List, Set, Tuple
from pathlib import Path

grid: List[str] = [
    "BEZC",
    "TQYA",
    "ASXO",
    "GJKM",
]


def dfs(
    graph: List[str],
    start: Tuple[int, int],
    path: List[str],
    seen: List[Tuple[int, int]],
    valid_words: Set[str],
) -> None:
    """
    Implements depth first search from a given starting node.
    """

    # Base case
    if start in seen:
        return

    # Create local copies of path and seen and add Node
    path: List[str] = path + [graph[start[0]][start[1]]]
    seen: List[Tuple[int, int]] = seen + [start]

    # Check if this is a valid word
    current_word: str = "".join(path)
    if len(path) >= 3 and current_word in WORDS:
        print(current_word)
        valid_words.add(current_word)

    up: Tuple[int, int] = (start[0] - 1, start[1])
    down: Tuple[int, int] = (start[0] + 1, start[1])

    left: Tuple[int, int] = (start[0], start[1] - 1)
    right: Tuple[int, int] = (start[0], start[1] + 1)

    diag_up_left: Tuple[int, int] = (start[0] - 1, start[1] - 1)
    diag_up_right: Tuple[int, int] = (start[0] - 1, start[1] + 1)

    diag_down_left: Tuple[int, int] = (start[0] + 1, start[1] - 1)
    diag_down_right: Tuple[int, int] = (start[0] + 1, start[1] + 1)

    possible_neighbors: List[Tuple[int, int]] = [
        up,
        down,
        right,
        left,
        diag_up_left,
        diag_up_right,
        diag_down_left,
        diag_down_right,
    ]

    for neighbor in possible_neighbors:
        if neighbor[0] < 0 or neighbor[0] >= len(graph):
            continue
        if neighbor[1] < 0 or neighbor[1] >= len(graph[0]):
            continue

        dfs(graph, neighbor, path, seen, valid_words)


def get_all_valid_words(graph: List[str], valid_words: Set[str]) -> None:
    # Loop over each node in the graph -> call walk (DFS)
    for y, row in enumerate(graph):
        for x, node in enumerate(row):
            dfs(graph, (y, x), [], [], valid_words)


def load_words_from_file() -> Set[str]:
    """
    Returns a set containing all words found in sowpods.txt.

    Note that "A" is not in this dataset.
    """
    SCRABBLE_PATH: Path = Path("Interview/tests/fixtures/sowpods.txt")
    words: Set[str] = set()

    with open(SCRABBLE_PATH, mode="r") as f:
        for line in f:
            words.add(line.strip())

    return words


if __name__ == "__main__":
    # Set of all valid words
    WORDS: Set[str] = load_words_from_file()
    # Pointer for valid words found in graph
    valid_words: Set[str] = set()
    # DFS
    get_all_valid_words(grid, valid_words)

    print(valid_words)
