def solution(num):
    for answer in range(500):
        if num == 1:
            return answer
        if num % 2 == 0:
            num //= 2
        else:
            num = 3*num + 1

    return -1
