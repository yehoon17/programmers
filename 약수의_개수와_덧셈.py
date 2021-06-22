def divisor(n):
    count = 1
    temp=1
    d=2
    while(n>1):
        if n%d == 0:
            n=n//d
            temp+=1
        else:
            count*=temp
            temp=1
            d+=1
    return count*temp
            

def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        count = divisor(n)
        if count%2 == 0:
            answer+=n
        else:
            answer-=n
    
    return answer
