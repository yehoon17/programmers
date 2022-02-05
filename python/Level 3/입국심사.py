def solution(n, times):
    i = 1
    while(True):
        if sum([i//time for time in times]) == n:
            break
        i += 1
        
    return i
