func solution(x int) bool {
    total := 0
    temp := x
    for x > 0 {
        total += x % 10
        x = int(x / 10)
    }
    if temp % total == 0 {
        return true
    } else {
        return false
    }
}
