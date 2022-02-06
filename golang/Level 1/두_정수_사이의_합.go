d49520375343func solution(a int, b int) int64 {
    var large, small int
    if a > b {
        large = a
        small = b
    } else {
        large = b
        small = a
    }
    
    return int64((small+large) * (1+large-small) / 2)
}
