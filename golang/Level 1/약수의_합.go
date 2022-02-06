func solution(n int) int {
    if n == 0 {
        return 0
    }
    
    var temp, p int
    
    answer := 1
    for d := 2; n != 1; d++ {
        temp = 1
        p = 1
        for n % d == 0 {
            temp += p * d
            p *= d
            n = int(n / d)
        }
        answer *= temp
    }
    return answer
}
