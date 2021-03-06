import (
    "strings"
    "strconv"
)
func solution(s string) string {
    max := -10000
    min := 10000
    for _, n := range strings.Split(s, " ") {
        number, _ := strconv.Atoi(n)
        if max < number {
            max = number
        }
        if min > number {
            min = number
        }
    }
    
    max_string := strconv.Itoa(max)
    min_string := strconv.Itoa(min)
    
    
    return min_string + " " + max_string
}