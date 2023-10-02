// Write a function that takes a string word as an argument
// and returns a count of all of the “A”s in that string.
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	s "strings"
)

func main() {

	// Collect command-line arguments
	var letter string
	var nSamples int64
	var piErr error

	if args := os.Args[1:]; len(args) == 0 {
		letter = "A"
		nSamples = 10
	} else {
		letter = s.ToUpper(args[0])
		nSamples, piErr = strconv.ParseInt(args[1], 10, 64)
		// Error handling for ParseInt
		check(piErr)
	}

	// Load data from a file into memory
	file, fErr := os.Open("More_Wordplay/tests/fixtures/sowpods.txt")
	check(fErr)
	defer file.Close()

	// Instantiate a scanner with the file
	scanner := bufio.NewScanner(file)

	// Instantiate a hash map
	countMap := make(map[string]int)

	// Loop over each word and add it's count to the hash map
	for scanner.Scan() {
		word := scanner.Text()
		count := countLetterInWord(word, letter)
		countMap[word] = count
	}

	// Error handling for scanner
	check(scanner.Err())

	// Sort the hash map by values and extract the top nSamples
	sortedKeys := sortMap(countMap)[0:nSamples]

	// Print the sorted hash map to std
	for _, k := range sortedKeys {
		fmt.Println(k, countMap[k])
	}

}

// Count all instances of the character 'a' in string
func countLetterInWord(word string, letter string) int {
	var counter int = 0
	for i := 0; i < len(word); i++ {
		if word[i] == letter[0] {
			counter += 1
		}
	}
	return counter

}

// Sort a hash map by values
func sortMap(target map[string]int) []string {
	// Extract the keys
	keys := make([]string, 0, len(target))

	// Iterate over the keys and add them to a new slice
	for key := range target {
		keys = append(keys, key)
	}

	// Sort the keys by value in descending order
	sort.SliceStable(keys, func(i, j int) bool {
		return target[keys[i]] > target[keys[j]]
	})

	return keys

}

// Generic error handling helper
func check(err error) {
	if err != nil {
		log.Fatal(err)
	}
}
