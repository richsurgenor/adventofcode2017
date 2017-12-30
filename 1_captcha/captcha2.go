package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
)

func main() {
	fmt.Printf("hello")
	// most obvious approach:
	// var total
	// variable blah
	// get the end of the list
	//
	// loop through all numbers in file
	// if blah is set then add numbers to total
	// after loop is finished check if last is same as first and if so add

	content, err := ioutil.ReadFile("input")
	steps := len(content) / 2

	if err != nil {
		log.Fatal(err)
	}

	var (
		total int = 0
	)

	for index, element := range content {
		elem, _ := strconv.Atoi(string(element))
		opposite, _ := strconv.Atoi(string(content[(index+steps)%(steps*2)]))
		if opposite == elem {
			total = total + elem
		}
		fmt.Printf("element: %d", elem)
	}

	fmt.Printf("Total sum: %d", total)
	//fmt.Printf("File contents: %s", content)
}
