def solution(dartResult):
    score = []
    i=0
    for _ in range(3):
        n=''
        while(True):
            if dartResult[i]>='0' and dartResult[i]<='9':
                n += dartResult[i]
                i+=1
            else:
                break
        n=int(n)
        power = 1
        if dartResult[i] == 'D':
            power=2
        elif dartResult[i] == 'T':
            power=3
        score.append(n**power)
        i+=1
        if i==len(dartResult):
            break
        if dartResult[i] == '*':
            i+=1
            score[-1]*=2
            if len(score)>1:
                score[-2]*=2
        elif dartResult[i] == '#':
            i+=1
            score[-1]*=-1
        
    return sum(score)
