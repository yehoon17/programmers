def dfs(begin, tickets, visited, count):
    min = ['ZZZ']
    for i, [dep, arr] in enumerate(tickets):
        if not visited[i]:
            if begin == dep:
                if count-1 == 0:
                    return [arr,begin]
                visited[i] = True
                temp = dfs(arr, tickets, visited, count-1)
                if min[-1] > temp[-1]:
                    min = temp
                visited[i] = False
    min.append(begin)
    return min

def solution(tickets):
    size = len(tickets)
    visited = [False for _ in range(size)]
    return dfs('ICN',tickets, visited, size)[::-1]
