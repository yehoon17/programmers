def solution(n):
    l = []
    while(n > 0):
        l.append(n % 3)
        n = n//3

    answer = 0
    x = 1
    for i in range(len(l)-1, -1, -1):
        answer += l[i] * x
        x *= 3
        
    return answer
