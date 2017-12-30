package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
)

func Main() {
	fmt.Printf("hello")
	// most obvious approach:
	// var total
	// variable blah
	// loop through all numbers in file
	// if blah is set then add numbers to total
	// after loop is finished check if last is same as first and if so add

	content, err := ioutil.ReadFile("input")
	if err != nil {
		log.Fatal(err)
	}

	var (
		last  int = -1
		total int = 0
	)

	for _, element := range content {
		elem, _ := strconv.Atoi(string(element))
		if last == elem {
			total = total + last
		}
		fmt.Printf("element: %d", elem)
		last = elem
	}

	if end, _ := strconv.Atoi(string(content[0])); last == end {
		total = total + int(content[0])
	}

	fmt.Printf("Total sum: %d", total)
	//fmt.Printf("File contents: %s", content)
}
