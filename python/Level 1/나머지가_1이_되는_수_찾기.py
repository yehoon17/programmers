def solution(n):
    i = 2
    while True:
        if n % i == 1:
            return i
        i += 1
