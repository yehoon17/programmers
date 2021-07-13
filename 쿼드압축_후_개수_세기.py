def solution(arr):
    answer = [0,0]
    size =  len(arr)//2
    neg = -5
    while(size>0):
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
        size//=2
    return answer
