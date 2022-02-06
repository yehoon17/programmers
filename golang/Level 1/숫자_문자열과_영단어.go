import "strings"


func solution(s string) int {
    strToNum := make(map[string]int)
    strToNum["zero"] = 0
    strToNum["one"] = 1
    strToNum["two"] = 2
    strToNum["three"] = 3
    strToNum["four"] = 4
    strToNum["five"] = 5
    strToNum["six"] = 6
    strToNum["seven"] = 7
    strToNum["eight"] = 8
    strToNum["nine"] = 9
    strToNum["0"] = 0
    strToNum["1"] = 1
    strToNum["2"] = 2
    strToNum["3"] = 3
    strToNum["4"] = 4
    strToNum["5"] = 5
    strToNum["6"] = 6
    strToNum["7"] = 7
    strToNum["8"] = 8
    strToNum["9"] = 9
    
    answer := 0
    for i := 0; i < len(s); {
        for str, num := range strToNum {
            if strings.HasPrefix(s[i:], str) {
                answer *= 10
                answer += num
                i += len(str)
                break
            }
        }
    }

    return answer
}
