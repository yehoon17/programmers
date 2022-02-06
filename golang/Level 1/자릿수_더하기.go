func solution(n int) int {
    answer := 0

    for n > 0 {
        answer += n % 10
        n = int(n / 10)
    }

    return answer
}
