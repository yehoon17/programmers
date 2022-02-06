func solution(n int, times []int) int64 {
    min := 1000000001
    max := 0
    for _, time := range times {
        if min > time {
            min = time
        }
        if max < time {
            max = time
        }
    }
    
    t := -1 * int(-n/len(times))
    start := t * min
    end := t * max
    
    var mid int
    var temp int
    for {
        mid = int((start+end)/2)
        temp = 0
        for _, time := range times {
            temp += int(mid/time)
        }

        if temp < n {
            start = mid
        } else {
            end = mid
        }
     
        if start + 1 == end {
            break
        }
    }
    
    return int64(end)
}