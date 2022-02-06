import "sort"

func solution(array []int, commands [][]int) []int {
    answer := []int{}
    var start, end, order int
    var temp []int
    
    for _, command := range commands {
        start = command[0]
        end = command[1]
        order = command[2]
        
        temp = []int{}
        for _, i := range array[start-1:end] {
            temp = append(temp, i)
        }
        sort.Ints(temp)
        
        answer = append(answer, temp[order-1])
    }
    
    return answer
}
