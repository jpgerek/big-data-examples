package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	reCleanLine := regexp.MustCompile(`[^a-záéíóúüñç\s]`)
	reSplitSpaces := regexp.MustCompile(`\s+`)
	for scanner.Scan() {
		line := reCleanLine.ReplaceAllString(strings.ToLower(scanner.Text()), "")
		if line == "" {
			continue
		}
		for _, word := range reSplitSpaces.Split(line, -1) {
			fmt.Printf("%s\t1\n", word)
		}
	}
}
