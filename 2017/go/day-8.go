package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func main() {
	bytes, _ := ioutil.ReadFile("2017/input/day-8.input")
	input := string(bytes)
	instructions := strings.Split(input, "\n")
	fmt.Print(instructions)
}
