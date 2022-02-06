func solution(clothes [][]string) int {
    answer := 1
    d := make(map[string]int)
    for _, cloth := range clothes {
        key := cloth[1]
        
        ok := false
        for t, _ := range d {
            if t == key {
                d[key]++
                ok = true
                break
            } 
        }
        if !ok {
            d[key] = 1
        }
    }
    
    for _, val := range d {
        answer *= val + 1
    }
    return answer - 1
}
