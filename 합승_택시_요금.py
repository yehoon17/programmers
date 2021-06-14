from collections import deque

def solution(n, s, a, b, fares):
    MAX_INT = 1000001
    costs = [[MAX_INT for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        costs[i][i] = 0
    
    for x,y,fare in fares:
        costs[x-1][y-1] = fare
        costs[y-1][x-1] = fare
    
    for start in (s-1,a-1,b-1,s-1,a-1,b-1):
        bfs = deque([start])
        visited = [False for _ in range(n)]
        while(bfs):
            now = bfs.popleft()
            visited[now] = True
            for i in range(n):
                if not visited[i]:
                    bfs.append(i)
                temp = costs[start][now]+costs[now][i]
                if costs[start][i] > temp:
                    costs[start][i] = temp
                    costs[i][start] = temp 
    
    answer = MAX_INT
    for i in range(n):
        temp = costs[s-1][i]+costs[a-1][i]+costs[b-1][i]
        if answer > temp:
            answer = temp
    
    return answer
