package main

import (
	"fmt"
	"io/ioutil"
	"reflect"
	"strconv"
    "strings"
)

func delete_empty (s []string) []string {
    var r []string
    for _, str := range s {
        if str != "" {
            r = append(r, str)
        }
    }
    return r
}

func main() {
	content, _ := ioutil.ReadFile("input")
    cont := string(content)
	fmt.Println(reflect.TypeOf(cont))

	var (
		total  int
	)

    rows := strings.Split(cont, "\n")
    rows = delete_empty(rows)
    for _, row := range rows {
        index := 0
        numbers := strings.Split(row, " ")
        numbers = delete_empty(numbers)
        for i := index; i < len(numbers) - 2; i++ {
            for j := index; j < len(numbers) - 1; j++ {
                num1, _ := strconv.Atoi(numbers[i])
                num2, _ := strconv.Atoi(numbers[j+1])

                fmt.Printf("num1: %d num2: %d\n", num1, num2)

                if a := num1 % num2; a == 0 {
                    fmt.Println("yee")
                    total += num1/num2 
                    // continue?
                }
                if a:= num2 % num1; a== 0 {
                    fmt.Println("yee")
                    total += num2/num1 
                }
            }
            index++
        }
	}

    fmt.Printf("This is the total: %d\n", total)
}

