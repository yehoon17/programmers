def solution(n):
    l=[]
    while(n>0):
        l.append(n%2)
        n//=2
    l.append(0)
    temp=l[:1]
    count = 0
    for i in range(1,len(l)):
        temp.append(l[i])
        if temp[i-1] == 1:
            count+=1
            if l[i] == 0:
                break
    size = len(temp)
    for i in range(size):
        if i >= count-1 and i < size-1:
            temp[i]=0
        else:
            temp[i]=1
    for i in range(size,len(l)):
        temp.append(l[i])
    answer=0
    m=1
    for n in temp:
        answer+=n*m
        m*=2
    return answer
