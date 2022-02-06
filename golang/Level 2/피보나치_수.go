func solution(n int) int {
    a := 0
    b := 1
    for i := 0; i < n-1; i++ {
        temp := a + b
        a = b
        b = temp % 1234567
    }
    
    return b
}
