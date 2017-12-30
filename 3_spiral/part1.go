package main

import (
    "fmt"
    "io/ioutil"
	"reflect"
    //"log"
    //"strconv"
)

func main() {
	content, _  := ioutil.ReadFile("input")

	fmt.Println(reflect.TypeOf(content))

    fmt.Println(string(content))
}
