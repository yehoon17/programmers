def solution(brown, yellow):
    sum=(4+brown)//2
    mult=brown+yellow
    for m in range(mult,0,-1):
        if mult%m == 0:
            n=mult//m
            if m+n == sum:
                break
    return [m,n]
