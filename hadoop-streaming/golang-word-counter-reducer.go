package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	result := map[string]int64{}

	for scanner.Scan() {
		line := scanner.Text()
		items := strings.Split(line, "\t")
		if len(items) != 2 {
			println("unexpected line format", line)
		}
		word := items[0]
		countStr := items[1]
		count, err := strconv.ParseInt(countStr, 10, 64)
		if err != nil {
			println(err)
			continue
		}
		_, exist := result[word]
		if !exist {
			result[word] = count
		} else {
			result[word] += count
		}
	}

	for word, countSum := range result {
		fmt.Printf("%s\t%d\n", word, countSum)
	}
}
