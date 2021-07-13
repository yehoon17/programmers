def solution(arr):
    answer = [0,0]
    size =  len(arr)
    neg = -5
    while(size>0):
        if arr == [[0]]:
            return [1,0]
        if arr == [[1]]:
            return [0,1]
        size//=2
        temp = [[neg for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                x, y = 2*i, 2*j
                tot = arr[x][y]+arr[x+1][y]+arr[x][y+1]+arr[x+1][y+1]
                if tot == 0:
                    temp[i][j] = 0
                elif tot == 4:
                    temp[i][j] = 1
                else:
                    for dx in range(2):
                        for dy in range(2):
                            val = arr[x+dx][y+dy]
                            if val>=0:
                                answer[val]+=1
        arr=temp
    
    return answer
