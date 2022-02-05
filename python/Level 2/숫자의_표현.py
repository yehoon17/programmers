def solution(n):
    answer = 1
    for a in range(1, n//2 + 1):
        temp = 2*n + a*a - a
        b = int(temp**0.5)
        if temp == b*b + b:
            answer += 1
            
    return answer
