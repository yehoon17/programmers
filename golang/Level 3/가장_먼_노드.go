func table(n int, edge [][]int) [][]bool {
    connected := make([][]bool, n)
    for i := range connected {
        connected[i] = make([]bool, n)
    }
    
    for _, points := range edge {
        connected[points[0]-1][points[1]-1] = true
        connected[points[1]-1][points[0]-1] = true
    }
    
    return connected
}

func solution(n int, edge [][]int) int {
    visited := make([]bool, n)
    visited[0] = true
    
    connected := table(n, edge)
    bfs := []int{0}
    for {
        next_bfs := []int{}
        for _, i := range bfs {
            for j, ok := range connected[i] {
                if ok && !visited[j] {
                    visited[j] = true
                    next_bfs = append(next_bfs, j)
                }
            }
        }
        if len(next_bfs) == 0 {
            break
        }
        bfs = next_bfs
    }
    
    return len(bfs)
}