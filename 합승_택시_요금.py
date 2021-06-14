from collections import deque

def solution(n, s, a, b, fares):
    MAX_INT = 10000000000000
    costs = [[MAX_INT for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        costs[i][i] = 0
    
    for x,y,fare in fares:
        costs[x-1][y-1] = fare
        costs[y-1][x-1] = fare
    
    for start in (s-1,a-1,b-1):
        bfs = deque([start])
        visited = [False for _ in range(n)]
        while(bfs):
            now = bfs.popleft()
            visited[now] = True
            for i in range(n):
                if not visited[i]:
                    bfs.append(i)
                costs[start][i] \
                = min(costs[start][i],
                      costs[start][now]\
                      +costs[now][i])
                costs[i][start] = costs[start][i] 
    
    answer = MAX_INT*n+1
    for i in range(n):
        answer = min(answer,
                     costs[s-1][i]+costs[a-1][i]+costs[b-1][i])
    
    return answer
