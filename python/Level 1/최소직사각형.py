def solution(sizes):
    long = 0
    short = 0
    for size in sizes:
        if long < max(size):
            long = max(size)
        if short < min(size):
            short = min(size)
            
    return long * short
