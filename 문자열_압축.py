def solution(s):
    size = len(s)
    answer = size
    for n in range(1,size//2+1):
        pats = []
        count = []
        i = 0
        while(True):
            pat = s[i:i+n]
            if pat == '':
                break
            if pats:
                if pats[-1] == pat:
                    count[-1]+=1
                else:
                    pats.append(pat)
                    count.append(1)
            else:
                pats.append(pat)
                count.append(1)
            i+=n
        temp = ''
        for pat,num in zip(pats,count):
            if num >1:
                temp += str(num)
            temp += pat
        if len(temp)<answer:
            answer=len(temp)
    return answer
                
