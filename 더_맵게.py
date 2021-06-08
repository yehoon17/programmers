def solution(scoville, K):
    answer = 0
    li = [x for x in scoville if x < K]
    hot = len(scoville) - len(li)
    li.sort(reverse = True)
    while(li):
        if len(li) == 1:
            # if one is not hot enough but at least is 
            if hot>1:
                return answer+1
            else:
                return -1
        temp = li.pop() + 2 * li.pop()
        if temp < K:
            li.append(temp)
            for i in  range(len(li)-1,0,-1):
                if li[i] > li[i-1]:
                    li[i],li[i-1] = li[i-1],li[i]
                else:
                    break
        else:
            hot+=1
        answer +=1
        
    return answer
