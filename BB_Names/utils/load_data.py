from collections import deque
import numpy as np


def load_list(file_path: str) -> list[str]:
    """
    This function takes a path to a data file as an input and returns that
    file as a list of strings.
    """
    with open(file_path, mode="r") as f:
        data: list[str] = f.read().splitlines()
    # Return the data as a list[str]
    return data


def load_set(file_path: str) -> set[str]:
    """
    This function takes a path to a data file as an input and returns that
    file as a set of strings.
    """
    with open(file_path, mode="r") as f:
        data: set[str] = set(f.read().splitlines())

    # Return the data as a set[str]
    return data


def load_dict(file_path: str) -> dict[str, bool]:
    """
    This function takes a path to a data file as an input and returns that
    file as a dictionary of file_line: True pairs.
    """
    with open(file_path, mode="r") as f:
        data: dict[str, bool] = dict.fromkeys(f.read.splitlines(), True)

    # Return the data as a dict[str, bool]
    return data


def load_tuple(file_path: str) -> tuple[str]:
    """
    This function takes a path to a data file as an input and returns that
    file as a tuple of strings.
    """
    with open(file_path, mode="r") as f:
        data: tuple[str] = tuple(f.read().splitlines())

    # Return the data as a tuple[str]
    return data


def load_frozen_set(file_path: str) -> frozenset[str]:
    """
    This function takes a path to a data file as an input and returns that
    file as a frozenset of strings.
    """
    with open(file_path, mode="r") as f:
        data: frozenset[str] = frozenset(f.read().splitlines())

    # Return the data as a frozenset[str]
    return data


def load_deque(file_path: str) -> deque[str]:
    """
    This function takes a path to a data file as an input and returns that
    file as a deque of strings.
    """
    with open(file_path, mode="r") as f:
        data: deque[str] = deque(f.read().splitlines())

    # Return the data as a deque[str]
    return data


def load_numpy_array(file_path: str) -> np.ndarray[str]:
    """
    This function takes a path to a data file as an input and returns that
    file as a np.ndarray of strings.
    """
    with open(file_path, mode="r") as f:
        data: np.ndarray[str] = np.array(f.read().splitlines(), dtype="O")

    # Return the data as a deque[str]
    return data


# priorty queue

# binary tree

# graph
