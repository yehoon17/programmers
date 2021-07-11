MAX_INT = 100000*200

def solution(n, s, a, b, fares):
    costs = [[MAX_INT for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        costs[i][i] = 0
    
    for x,y,fare in fares:
        costs[x-1][y-1] = fare
        costs[y-1][x-1] = fare
    
    for i in range(n):
        for k in range(n):
            for j in range(n):
                if costs[i][k] > costs[i][j] + costs[j][k]:
                    costs[i][k] = costs[i][j] + costs[j][k]
                    costs[k][i] = costs[i][j] + costs[j][k]
                    
    for i in range(n):
        for k in range(n):
            for j in range(n):
                if costs[i][k] > costs[i][j] + costs[j][k]:
                    costs[i][k] = costs[i][j] + costs[j][k]
    
    answer = MAX_INT
    for i in range(n):
        temp = costs[i][a-1] + costs[i][b-1] + costs[s-1][i]
        if answer > temp:
            answer = temp
    
    return answer
