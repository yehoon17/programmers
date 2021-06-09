def solution(info, query):
    answer = []
    infolist = []
    scores = []
    for x in info:
        xlist = x.split()
        scores.append(int(xlist[-1]))
        xlist = list(map(lambda a:a[0],xlist[:-1]))
        infolist.append(xlist)
    for q in query:
        qlist = q.split()
        count = 0
        temp = []
        for i in range(4):
            temp.append(qlist[i*2][0])
        qscore = int(qlist[-1])
        for xlist,score in zip(infolist,scores):
            flag = True
            if qscore > score:
                continue
            for i in range(4):
                if temp[i] == '-':
                    pass
                elif temp[i] != xlist[i]:
                    flag = False
                    break
            if flag:
                count+=1
            
        answer.append(count)
    
    return answer
