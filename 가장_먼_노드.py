def tablize(n, edge):
    table = [[0 for _ in range(n)] for _ in range(n)]
    
    for i,j in edge:
        table[i-1][j-1] = 1
        table[j-1][i-1] = 1
        
    return table

def solution(n, edge):
    visited = [False for _ in range(n)]
    visited[0] = True
    
    graph = tablize(n, edge)
    bfs = [0]
    while True:
        next_bfs = []
        for i in bfs:
            connected = [j for j in range(n) if graph[i][j] == 1]
            for j in connected:
                if not visited[j]:
                    visited[j] = True
                    next_bfs.append(j)
        if not next_bfs:
            break
        bfs = next_bfs
    
    return len(bfs)
