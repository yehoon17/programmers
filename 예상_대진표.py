def solution(n,a,b):
    answer = 0
    large=max(a,b)
    small=min(a,b)
    while(True):
        answer+=1
        if large%2==0 and large==small+1:
            break
        large=(large+1)//2
        small=(small+1)//2

    return answer
