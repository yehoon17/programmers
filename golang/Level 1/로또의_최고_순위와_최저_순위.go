func solution(lottos []int, win_nums []int) []int {
    cnt := 0
    zero := 0
    
    for _, n := range lottos {
        if n == 0 {
            zero++
        } else {
            for _, win_num := range win_nums {
                if n == win_num {
                    cnt++
                    break
                }
            }
        }
    }
    
    highRank := 7 - cnt - zero
    lowRank := 7 - cnt
    if highRank > 6 {
        highRank = 6
    }
    if lowRank > 6 {
        lowRank = 6
    }
    
    return []int{highRank, lowRank}
}