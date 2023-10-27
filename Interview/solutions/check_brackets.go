package main

import "fmt"

func main() {
	// Test examples
	e1 := "{[()]}"
	e2 := "{[(])}"
	e3 := "[(){()}"
	e4 := ")"

	// Calls
	fmt.Println(checkBrackets((e1)))
	fmt.Println(checkBrackets((e2)))
	fmt.Println(checkBrackets((e3)))
	fmt.Println(checkBrackets((e4)))
}

func checkBrackets(input string) bool {
	// Odd length strings are always unbalanced
	if len(input)%2 != 0 {
		return false
	}

	openingBrackets := map[rune]bool{
		'{': true,
		'[': true,
		'(': true,
	}

	pairs := map[rune]rune{
		')': '(',
		'}': '{',
		']': '[',
	}

	stack := newStack()

	// Loop over each rune in input string
	for _, runeVal := range input {
		// Opening bracket
		present, _ := openingBrackets[runeVal]
		if present {
			stack.push(runeVal)
		} else {
			// Closing bracket
			if stack.Length == 0 {
				return false
			}
			// Pop prev opening bracket from stack
			prevOpeningBracket := stack.pop()
			if pairs[runeVal] != prevOpeningBracket {
				return false
			}
		}
	}

	if stack.Length > 0 {
		return false
	}

	return true
}

// QNode
type Node struct {
	value rune
	prev  *Node
}

// Stack
type Stack struct {
	Length int
	head   *Node
}

func newStack() *Stack {
	stack := Stack{Length: 0, head: nil}
	return &stack
}

func (stack *Stack) push(item rune) {
	// Instatiate a new Node
	node := Node{value: item}

	// Incremement length
	stack.Length++

	// If this is the first push
	if stack.Length == 1 {
		stack.head = &node
		return
	}

	// Point the head to previous
	node.prev = stack.head
	stack.head = &node
}

func (stack *Stack) pop() rune {
	// Decrement count
	stack.Length = max(0, (stack.Length - 1))

	// Save out a reference to the head
	head := stack.head

	// Head is last value
	if stack.Length == 0 {
		stack.head = nil
		return head.value
	}

	// Set the head to the previous Node
	stack.head = head.prev

	return head.value
}

func (stack *Stack) peek() rune {
	return stack.head.value
}
