def solution(info, query):
    answer = []
    
    d = {}
    for lang in ('cpp', 'java', 'python'):
        d[lang] = {}
        for job in ('backend','frontend'):
            d[lang][job] = {}
            for exp in ('junior','senior'):
                d[lang][job][exp] = {}
                for food in ('chicken','pizza'):
                    d[lang][job][exp][food] = []
    
    for x in info:
        xlist = x.split()
        d[xlist[0]][xlist[1]][xlist[2]][xlist[3]].append(int(xlist[4]))
        
    for q in query:
        temp = q.split()
        count = 0
        qlist = [temp[i*2] for i in range(4)]
        qscore = int(temp[-1])
        temp = [d]
        for i in range(4):
            if qlist[i] == '-':
                temp = [t[k] for t in temp for k in t]
            else:
                temp = [t[qlist[i]] for t in temp]
        for t in temp:
            for score in t:
                if score >= qscore:
                    count+=1
        answer.append(count)
    
    return answer
