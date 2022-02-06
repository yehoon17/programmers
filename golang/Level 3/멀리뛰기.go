func solution(n int) int64 {
    if n == 1 {
        return int64(1)
    }
    
    a := 1
    b := 2
    var temp int
    for i := 2; i < n; i++ {
        temp = a + b
        a = b
        b = temp % 1234567
    }
    
    return int64(b)
}
