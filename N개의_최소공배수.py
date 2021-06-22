def gcd(a,b):
    while(True):
        large = max(a,b)
        small = min(a,b)
        if large%small == 0:
            return small
        a=large-small
        b=small

def solution(arr):
    a = arr.pop()
    while(arr):
        b = arr.pop()
        d = gcd(a,b)
        a = a*b//d
    return a
