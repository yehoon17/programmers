func solution(num int) int {
    for answer := 0; answer < 500; answer++ {
        if num == 1 {
            return answer
        } 
        
        if num % 2 == 0 {
            num = num / 2
        } else {
            num = 3*num + 1
        }
    }
    
    return -1
}
