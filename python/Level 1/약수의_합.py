def solution(n):
    if n == 0:
        return 0

    answer, d = 1, 2
    while n != 1:
        temp, p = 1, 1
        while n % d == 0:
            temp += p * d
            p *= d
            n //= d
            
        answer *= temp
        d += 1

    return answer
