from itertools import permutations

def solution(n, k):
    l=[i for i in range(1,1+n)]
    a=0
    for p in permutations(l):
        a+=1
        if a==k:
            return list(p)
