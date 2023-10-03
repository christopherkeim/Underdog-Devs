// Solution 5: What are all of the compound words? These are words made
// up of 2 smaller words. For example, “SNOWMAN” is a compound word made
// from “SNOW” and “MAN”, and “BEACHBALL” is a compound word made from
// “BEACH” and “BALL”.
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	// Load the file into a hash map set implementation
	dataMap := loadFileIntoMapSet("Bigger_Wordplay/tests/fixtures/sowpods.txt")

	// Extract all the compound words from the data
	compoundWords := getAllCompoundWords(dataMap)

	// Print the compound words to std
	for _, word := range compoundWords {
		fmt.Println(word)
	}
}

// Load file into hash map (set)
func loadFileIntoMapSet(path string) map[string]bool {
	// Load data from a file into memory
	file, fErr := os.Open(path)
	check(fErr)
	defer file.Close()

	// Instantiate a scanner with the file
	scanner := bufio.NewScanner(file)

	// Instantiate a hash map to store our data in
	dataMap := make(map[string]bool)

	// Loop over each word and add it to the hash map
	for scanner.Scan() {
		word := scanner.Text()
		dataMap[word] = true
	}

	// Error handling for scanner
	check(scanner.Err())

	return dataMap
}

// Discover and extract all of the compound words in a dataset
func getAllCompoundWords(dataMap map[string]bool) []string {
	// Instantiate an empty map for our matches
	matches := make(map[string]bool)

	// Loop over each word in the hash map
	for word := range dataMap {
		pointer := 1
		// Scan the word to discover the first substring compound
		for pointer < len(word) {
			currCompound := word[0:pointer]
			// Check for presence in data hash map
			present, _ := dataMap[currCompound]
			if present {
				// Extract the second potential compound
				secondCompound := word[pointer:]
				// Check for presence in data hash map
				present, _ = dataMap[secondCompound]
				if present {
					matches[word] = true
				}
			}
			pointer += 1
		}
	}
	// Define a slice to hold the compound words
	compoundWords := make([]string, 0, len(matches))

	// Extract the keys and add them to the slice
	for key := range matches {
		compoundWords = append(compoundWords, key)
	}
	return compoundWords
}

// Generic error handling helper
func check(err error) {
	if err != nil {
		log.Fatal(err)
	}
}
