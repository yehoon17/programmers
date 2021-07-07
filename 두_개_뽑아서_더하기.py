from itertools import combinations

def solution(numbers):
    s = set()
    for x,y in combinations(numbers,2):
        s.add(x+y)
    return sorted(list(s))
