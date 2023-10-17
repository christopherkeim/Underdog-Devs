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
	fmt.Println("Sorted and deduped array: ", root.inOrderTraversal())
	fmt.Println()

	// Delete
	root.delete(5)
	fmt.Println("BST after deleting 5: ", root.inOrderTraversal())
	fmt.Println("5 in BST: ", root.exists(5))
	fmt.Println("9 in BST: ", root.exists(9))
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

func (r *BinarySearchTree) insert(value int) {
	// No duplicates in BST
	if value == r.value {
		return
	}

	// Smaller values are pushed down left subtree
	if value < r.value {
		if r.left != nil {
			r.left.insert(value)
		} else {
			r.left = newBinarySearchTree(value, nil, nil)
		}
	}

	// Larger values are pushed down right subtree
	if value > r.value {
		if r.right != nil {
			r.right.insert(value)
		} else {
			r.right = newBinarySearchTree(value, nil, nil)
		}
	}
}

func (r *BinarySearchTree) delete(value int) *BinarySearchTree {
	if value < r.value {
		if r.left != nil {
			r.left = r.left.delete(value)
			return r
		}
	} else if value > r.value {
		if r.right != nil {
			r.right = r.right.delete(value)
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
		minValue := r.right.getMin()
		r.value = minValue
		r.right = r.right.delete(minValue)

	}
	return r
}

func (r *BinarySearchTree) exists(value int) bool {
	// Predicate function that returns truth of membership for a given
	// for a given value in the Binary Search Tree
	if value == r.value {
		return true

	} else if value < r.value {
		if r.left == nil {
			return false
		}
		return r.left.exists(value)

	} else if value > r.value {
		if r.right == nil {
			return false
		}
		return r.right.exists(value)

	} else {
		return false
	}
}

func (r *BinarySearchTree) getMin() int {
	if r.left == nil {
		return r.value
	}
	return r.left.getMin()
}

func (r *BinarySearchTree) getMax() int {
	if r.right == nil {
		return r.value
	}
	return r.right.getMax()
}

func (r *BinarySearchTree) inOrderTraversal() []int {
	/*
			Depth first search traversal: left subtree always comes first, with
		    right subtree as second.

		    Returns sorted and deduped / unique elements in the array.
	*/
	elements := make([]int, 0, 10)

	// First visit left subtree
	if r.left != nil {
		elements = append(elements, r.left.inOrderTraversal()...)
	}

	// Next visit root
	elements = append(elements, r.value)

	// Finally visit right subtree
	if r.right != nil {
		elements = append(elements, r.right.inOrderTraversal()...)
	}

	return elements
}

func buildTree(arr []int) *BinarySearchTree {
	// Helper function for building a tree from an array
	// Root node
	root := newBinarySearchTree(arr[0], nil, nil)

	for i := 1; i < len(arr); i++ {
		root.insert(arr[i])
	}

	return root
}
