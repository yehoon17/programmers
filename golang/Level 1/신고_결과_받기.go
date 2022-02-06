import (
    "strings"
)

func removeDuplicateStr(strSlice []string) []string {
    allKeys := make(map[string]bool)
    list := []string{}
    for _, item := range strSlice {
        if _, value := allKeys[item]; !value {
            allKeys[item] = true
            list = append(list, item)
        }
    }
    return list
}

func solution(id_list []string, reports []string, k int) []int {
    reports = removeDuplicateStr(reports)
    
    reported_by := make(map[string]map[string]bool)
    for _, id := range id_list {
        reported_by[id] = make(map[string]bool)
    }
    
    n_reports := make(map[string]int)
    for _, id := range id_list {
        n_reports[id] = 0
    }
    
    for _, report := range reports {
        slice := strings.Split(report, " ")
        reporter := slice[0]
        reported := slice[1]
        
        n_reports[reported] += 1
        reported_by[reporter][reported] = true
    }
    
    n_emails := make([]int, len(id_list))
    for i, user := range id_list {
        for reported, _ := range reported_by[user] {
            if n_reports[reported] >= k {
                n_emails[i]++
            }
        }
    }
    
    return n_emails
}