def solution(s):
    zeros = s.count('0')
    n = s.count('1')

    if n == 1:
        if zeros > 0:
            return [1, zeros]
        else:
            return [0, 0]

    repeat = 1
    while n != 1:
        ones = 0
        while n != 0:
            if n % 2 == 0:
                zeros += 1
            else:
                ones += 1
                
            n //= 2

        repeat += 1
        n = ones

    return [repeat, zeros]
