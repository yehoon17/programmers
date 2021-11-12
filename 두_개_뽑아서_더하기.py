from itertools import combinations

def solution(numbers):
    return sorted(list({x + y for x, y in combinations(numbers, 2)}))
