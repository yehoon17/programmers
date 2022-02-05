def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            bfs = [i]
            while bfs:
                temp = bfs.pop()
                visited[temp] = True
                for j in range(n):
                    if computers[temp][j] == 1 and not visited[j]:
                        bfs.append(j)
            answer += 1
    return answer
