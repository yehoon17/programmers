func min_idx(arr []int) int {
    idx := 0
    
    for i, val := range arr {
        if i == 0 {
            continue 
        }
        if val < arr[idx] {
            idx = i
        }
    }
    
    return idx
}

func solution(arr []int) []int {
    if len(arr) == 1 {
        return []int{-1}
    }
    
    idx := min_idx(arr)
    
    return append(arr[:idx], arr[idx+1:]...)
}
