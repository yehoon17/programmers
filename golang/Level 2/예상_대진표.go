func solution(n int, a int, b int) int {
    answer := 0
    var large, small int
    
    if a > b {
        large = a
        small = b
    } else {
        large = b
        small = a
    }
    
    for {
        answer++
        if large % 2 == 0 && large == small + 1 {
            break
        }
        large = int((large + 1)/2)
        small = int((small + 1)/2)
    }

    return answer
}
