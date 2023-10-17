// Binary Search Tree implementation.
package main

import (
	"fmt"
)

func main() {
	// Testing for integer slice
	a := []int{5, 16, 7, 9, -1, 4, 3, 11, 11, 2}
	root := buildTree(a)

	// In order traversal
	fmt.Println("Sorted and deduped array: ", inOrderTraversal(root))
	fmt.Println()

	// Delete
	delete(root, 5)
	fmt.Println("BST after deleting 5: ", inOrderTraversal(root))
	fmt.Println("5 in BST: ", exists(root, 5))
	fmt.Println("9 in BST: ", exists(root, 9))
}

type BinarySearchTree struct {
	value int
	left  *BinarySearchTree
	right *BinarySearchTree
}

func newBinarySearchTree(value int, left *BinarySearchTree, right *BinarySearchTree) *BinarySearchTree {
	root := BinarySearchTree{value: value, left: left, right: right}
	return &root
}

func insert(r *BinarySearchTree, value int) {
	// No duplicates in BST
	if value == r.value {
		return
	}

	// Smaller values are pushed down left subtree
	if value < r.value {
		if r.left != nil {
			insert(r.left, value)
		} else {
			r.left = newBinarySearchTree(value, nil, nil)
		}
	}

	// Larger values are pushed down right subtree
	if value > r.value {
		if r.right != nil {
			insert(r.right, value)
		} else {
			r.right = newBinarySearchTree(value, nil, nil)
		}
	}
}

func delete(r *BinarySearchTree, value int) *BinarySearchTree {
	if value < r.value {
		if r.left != nil {
			r.left = delete(r.left, value)
			return r
		}
	} else if value > r.value {
		if r.right != nil {
			r.right = delete(r.right, value)
			return r
		}
	} else {
		if r.left == nil && r.right == nil {
			return nil
		}
		if r.left == nil {
			return r.right
		}
		if r.right == nil {
			return r.left
		}
		minValue := getMin(r.right)
		r.value = minValue
		r.right = delete(r.right, minValue)

	}
	return r
}

func exists(r *BinarySearchTree, value int) bool {
	// Predicate function that returns truth of membership for a given
	// for a given value in the Binary Search Tree
	if value == r.value {
		return true
	} else if value < r.value {
		if r.left == nil {
			return false
		}
		return exists(r.left, value)
	} else if value > r.value {
		if r.right == nil {
			return false
		}
		return exists(r.right, value)
	} else {
		return false
	}
}

func getMin(r *BinarySearchTree) int {
	if r.left == nil {
		return r.value
	}
	return getMin(r.left)
}

func getMax(r *BinarySearchTree) int {
	if r.right == nil {
		return r.value
	}
	return getMax(r.right)
}

func inOrderTraversal(r *BinarySearchTree) []int {
	/*
			Depth first search traversal: left subtree always comes first, with
		    right subtree as second.

		    Returns sorted and deduped / unique elements in the array.
	*/
	elements := make([]int, 0)

	// First visit left subtree
	if r.left != nil {
		elements = append(elements, inOrderTraversal(r.left)...)
	}

	// Next visit root
	elements = append(elements, r.value)

	// Finally visit right subtree
	if r.right != nil {
		elements = append(elements, inOrderTraversal(r.right)...)
	}

	return elements
}

func buildTree(arr []int) *BinarySearchTree {
	// Helper function for building a tree from an array
	// Root node
	root := newBinarySearchTree(arr[0], nil, nil)

	for i := 1; i < len(arr); i++ {
		insert(root, arr[i])
	}

	return root
}
