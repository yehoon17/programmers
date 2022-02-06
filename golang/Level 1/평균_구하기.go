func solution(arr []int) float64 {
    total := 0
    for _, n := range arr {
        total += n
    }
    
    return float64(total) / float64(len(arr))
}
