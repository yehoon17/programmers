func gcd(a int, b int) int {
    var large int
    var small int
    
    for {
        if a > b {
            large = a
            small = b
        } else {
            large = b
            small = a
        }
        if large % small == 0 {
            return small
        }
        a = large - small
        b = small
    }
}

func solution(w int, h int) int64 {
    var answer int64
    d := gcd(w, h)
    answer = int64(w*h) - (int64(w/d) + int64(h/d) - 1)*int64(d)
    return answer
}