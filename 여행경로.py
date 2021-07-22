def dfs(begin, tickets, visited, count):
    min = ['ZZZ']
    flag = False
    for i, [dep, arr] in enumerate(tickets):
        if not visited[i]:
            if begin == dep:
                if count-1 == 0:
                    return [arr,begin]
                visited[i] = True
                temp = dfs(arr, tickets, visited, count-1)
                if temp:
                    if min[-1] > temp[-1]:
                        flag = True
                        min = temp
                visited[i] = False
    if flag:    
        min.append(begin)
        return min
    return []
    
def solution(tickets):
    size = len(tickets)
    visited = [False for _ in range(size)]
    return dfs('ICN',tickets, visited, size)[::-1]

solution([["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]])
