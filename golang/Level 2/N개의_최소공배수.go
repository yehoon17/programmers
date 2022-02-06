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
        
        a = large - small
        b = small
    }
}

func solution(arr []int) int {
    a := arr[len(arr)-1]
    for i := len(arr)-2; i > -1; i-- {
        b := arr[i]
        d := gcd(a, b)
        a = int(a * b / d)
    }
    return a
}
