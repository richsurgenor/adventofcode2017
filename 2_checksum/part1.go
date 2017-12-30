package main

import (
	"fmt"
	"io/ioutil"
	"reflect"
	"strconv"
)

func main() {
	content, _ := ioutil.ReadFile("input")
	fmt.Println(reflect.TypeOf(content))

	var (
		total  int
		number string
		small  int
		big    int
	)

	for _, char := range string(content) {
		switch char {
		case ' ':
			num, _ := strconv.Atoi(number)
			fmt.Printf("This is the actual number %d\n", num)
			if small == 0 || num < small {
				small = num
			}
			if num > big {
				big = num
			}
			number = ""
		case '\n':
			total += big - small
			small = 0
			big = 0
		default:
			number += string(char)
		}
	}

	fmt.Printf("This is the total: %d\n", total)
}
