def solution(name):
    answer = 0
    isStart = True
    indexA = []
    lenA = []
    for i,c in enumerate(name):
        temp = ord(c) - ord('A')
        answer += min(temp,26-temp)
        if temp == 0:
            if isStart:
                isStart = False
                indexA.append(i)
                count = 1
            else:
                count+=1
        else:
            if not isStart:
                isStart = True
                lenA.append(count)
    size = len(name)
    dist = size-1
    for i, n in zip(indexA, lenA):
        distF = i-1
        distB = size-i-n
        dist = min(dist,min(distF,distB)+distF+distB)
        
    answer+=dist
    return answer
