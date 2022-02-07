func gcd(a int, b int) int {
    var large, small int
    
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
        
        a = large % small
        b = small
    }
}


func solution(n int, m int) []int {
    d := gcd(n, m)
    return []int{d, n*m / d}
}
