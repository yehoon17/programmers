func solution(s string) []int {
    zeros := 0
    n := 0
    
    for _, digit := range s {
        if digit == '0' {
            zeros++
        } else {
            n++
        }
    }
    
    if n == 1 {
        if zeros > 0 {
            return []int{1, zeros}
        } else {
            return []int{0, 0}
        }
    }
    
    cnt := 1
    for n != 1 {
        ones := 0
        for n != 0 {
            if n % 2 == 0 {
                zeros++
            } else {
                ones++
            }
            n /= 2
        }
        cnt++
        n = ones
    }
    return []int{cnt, zeros}
}