def solution(n, lost, reserve):
    answer = n
    isLost = [False for _ in range(n)]
    for i in lost:
        isLost[i-1] = True
        answer-=1
        
    isReserve = [False for _ in range(n)]
    for i in reserve:
        isReserve[i-1] = True
        
    for i in range(n):
        if isLost[i] and isReserve[i]:
            isLost[i] = False
            isReserve[i] = False
            answer+=1
    
    if isReserve[0] and isLost[1]:
        isReserve[0] = False
        isLost[1] = False
        answer+=1
    if isReserve[-1] and isLost[-2]:
        isReserve[-1] = False
        isLost[-2] = False
        answer+=1
    for i in range(1,n-1):
        if isReserve[i]:
            if isLost[i-1] and not isLost[i+1]:
                isReserve[i] = False
                isLost[i-1] = False
                answer+=1
            elif isLost[i+1] and not isLost[i-1]:
                isReserve[i] = False
                isLost[i+1] = False
                answer+=1
            
    for i in range(1,n-1):
        if isReserve[i]:
            if isLost[i-1] and isLost[i+1]:
                isReserve[i] = False
                isLost[i-1] = False
                answer+=1
                
    return answer
