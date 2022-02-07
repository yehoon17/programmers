def gcd(a, b):
    while True:
        if a > b:
            large, small = a, b
        else:
            large, small = b, a

        if large % small == 0:
            return small

        a = large % small
        b = small


def solution(n, m):
    d = gcd(n, m)
    return [d, n*m // d]
