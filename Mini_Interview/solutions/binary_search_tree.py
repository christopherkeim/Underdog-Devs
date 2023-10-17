"""
Binary search tree implementation

A Binary Search Tree (BST) is a tree where each Node is a value greater
than all of its left child nodes and less than all of its right child nodes.

Binary trees are useful for storing data in an organized manner so that it can 
be quickly retrieved, inserted, updated, and deleted. This arrangement of nodes 
allows each comparison to skip about half of the rest of the tree.

Time Complexity:

Binary search trees provide an average Big-O complexity of O(log(n)) for search, 
insert, update, and delete operations. log(n) is much faster than the linear O(n) 
time required to find elements in an unsorted array. Many popular production databases 
such as PostgreSQL and MySQL use binary trees under the hood to speed up CRUD 
operations.
"""
from __future__ import annotations
from typing import List, Optional


class BinarySearchTreeNode:
    def __init__(self, value: int | str) -> BinarySearchTreeNode:
        self.value = value
        self.left: Optional[BinarySearchTreeNode] = None
        self.right: Optional[BinarySearchTreeNode] = None

    def insert(self, value) -> None:
        # No duplicates in BST
        if value == self.value:
            return None

        # Smaller values are pushed down left subtree
        if value < self.value:
            # If a tree node already exists left, recursively down it
            if self.left is not None:
                self.left.insert(value)
            # Otherwise, add this smaller value into the BST as a node
            else:
                self.left = BinarySearchTreeNode(value)

        # Larger values are pushed down right subtree
        else:
            # If a tree node already exists right, recursive down it
            if self.right is not None:
                self.right.insert(value)
            # Otherwise, add this larger value into the BST as a node
            else:
                self.right = BinarySearchTreeNode(value)

    def delete(self, value: int | str) -> BinarySearchTreeNode:
        if value < self.value:
            if self.left is not None:
                self.left = self.left.delete(value)
                return self

        elif value > self.value:
            if self.right is not None:
                self.right = self.right.delete(value)
                return self

        else:
            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right

            if self.right is None:
                return self.left

            min_value: int | float = self.right.get_min()
            self.value = min_value
            self.right = self.right.delete(min_value)

        return self

    def exists(self, value: int | str) -> bool:
        """
        Search predicate function that returns truth of membership for a given
        value in the Binary Search Tree.
        """
        if value == self.value:
            return True

        # If the value is less than the current node, search left
        if value < self.value:
            if self.left is None:
                return False

            return self.left.exists(value)

        # If value is greater than current node, search right
        if value > self.value:
            if self.right is None:
                return False

            return self.right.exists(value)

    def get_min(self) -> int | str:
        """
        This can be implemented iteratively by using the condition
        `while self.left is not None:`
        """
        if self.left is None:
            return self.value

        return self.left.get_min()

    def get_max(self) -> int | str:
        if self.right is None:
            return self.value

        return self.right.get_max()

    def in_order_traversal(self) -> List[int | str]:
        """
        Depth first search traversal: left subtree always comes first, with
        right subtree as second.

        Returns sorted and deduped / unique elements in the array.
        """
        elements: List[int | str] = []

        # First visit left subtree
        if self.left is not None:
            elements.extend(self.left.in_order_traversal())

        # Next visit nroot
        elements.append(self.value)

        # Finally visit right subtree
        if self.right is not None:
            elements.extend(self.right.in_order_traversal())

        return elements


def build_tree(array: List[int | str]) -> BinarySearchTreeNode:
    """
    Helper function for building a tree from an array.
    """
    # Root node
    root: BinarySearchTreeNode = BinarySearchTreeNode(array[0])

    # Loop over remaining elements in array
    for i in range(1, len(array)):
        root.insert(array[i])

    return root


if __name__ == "__main__":
    # Testing for numerical arrays
    numerical_array: List[int] = [5, 16, 7, 9, -1, 4, 3, 11, 11, 2]
    nroot: BinarySearchTreeNode = build_tree(numerical_array)

    print(f"Sorted and deduped array: {nroot.in_order_traversal()}")

    nroot.delete(5)
    print(f"BST after deleting 5: {nroot.in_order_traversal()}")
    print(f"5 in BST: {nroot.exists(5)}")
    print(f"9 in BST: {nroot.exists(9)}\n")

    # Testing for alpha arrays
    alpha_array: List[str] = [
        "Banana",
        "Orange",
        "Apple",
        "Apple",
        "Pear",
        "Watermelon",
        "Plum",
    ]
    aroot: BinarySearchTreeNode = build_tree(alpha_array)

    print(f"Sorted and deduped array: {aroot.in_order_traversal()}")

    aroot.delete("Orange")
    print(f"BST after deleting Orange: {aroot.in_order_traversal()}")
    print(f"Orange in BST: {aroot.exists('Orange')}")
    print(f"Pear in BST: {aroot.exists('Pear')}\n")
