def solution(genres, plays):
    answer = []
    size = len(genres)
    total = {}
    topTwo = {}  
    
    for i in range(size):
        g = genres[i]
        p = plays[i]
        if g in total:
            total[g]+=p
        else:
            total[g] = p
        if g in topTwo:
            temp = topTwo[g]
            if len(temp) == 1:
                if temp[0][1] > p:
                    temp.append([i,p])
                else:
                    t = [[i,p],temp[0]]
                    topTwo[g] = t
            else:
                if temp[0][1] < p:
                    t = [[i,p],temp[0]]
                    topTwo[g] = t
                elif temp[1][1] < p:
                    temp[1] = [i,p]
        else:
            topTwo[g] = [[i,p]]
#    print(total)
#    print(topTwo)
    keys = list(total.keys())
    keys.sort(key = lambda x: total[x], reverse = True)
    for k in keys:
        for i in range(len(topTwo[k])):
            answer.append(topTwo[k][i][0])
        
    return answer
