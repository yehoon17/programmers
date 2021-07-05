def solution(dirs):
    answer = 0
    visitedV = [[False]*10 for _ in range(11)]
    visitedH = [[False]*11 for _ in range(10)]
    x,y=0,0
    for d in dirs:
        if d == "U":
            if x<5:
                if not visitedV[x][y]:
                    visitedV[x][y] = True
                    answer+=1
                x+=1
        elif d == "D":
            if x>-5:
                x-=1
                if not visitedV[x][y]:
                    visitedV[x][y] = True
                    answer+=1
        elif d == "R":
            if y<5:
                if not visitedV[x][y]:
                    visitedH[x][y] = True
                    answer+=1
                y+=1
        elif d == "L":
            if y>-5:
                y-=1
                if not visitedV[x][y]:
                    visitedH[x][y] = True
                    answer+=1
    
    return answer
