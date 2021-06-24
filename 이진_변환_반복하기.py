def solution(s):
    zeros=s.count('0')
    n=s.count('1')
    if n==1:
        if zeros>0:
            return [1,zeros]
        else:
            return [0,0]
    repeat=1
    while(True):
        temp=0
        while(True):
            if n%2==0:
                zeros+=1
            else:
                temp+=1
            n//=2
            if n==0:
                break
        n=temp
        repeat+=1
        if temp==1:
            break
    return[repeat,zeros]
