func solution(numbers []int) int {
    total := 45
    for _, number := range numbers {
        total -= number
    }
    return total
}