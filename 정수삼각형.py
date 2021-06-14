def solution(triangle):
    size = len(triangle)
    for i in range(1,size): 
        for j in range(i+1):
            temp = 0
            if j>0:
                temp = max(temp, triangle[i-1][j-1])
            if j<i:
                temp = max(temp, triangle[i-1][j])
            triangle[i][j] += temp            
    return max(triangle[size-1])
