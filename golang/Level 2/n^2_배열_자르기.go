func solution(n int, left int64, right int64) []int {
    answer := []int{}
    var max int
    for i := int(left); i <= int(right); i++ {
        if int(i/n) > i % n {
            max = int(i/n)
        } else {
            max = i % n
        }
        answer = append(answer, 1 + max)
    }
    return answer
}
