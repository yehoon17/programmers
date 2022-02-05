def solution(cookie):
    size = len(cookie)
    temp = [[0 for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            if j == 0:
                temp[i][i+j] = cookie[i]
            elif i+j<size:
                temp[i][i+j] = temp[i][i+j-1]+cookie[i+j]
            else:
                k = size-j-1
                temp[i][k] = temp[i][k+1]+cookie[k]
                
    answer = 0
    for i in range(size):
        for j in range(i,size):
            for k in range(j+1,size):
                if temp[i][j] == temp[j+1][k]:
                    answer+=1
                    break
    return answer
