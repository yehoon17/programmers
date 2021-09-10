from heapq import heappush, heappop

def solution(scoville, K):
    cnt = 0
    h = []
    for x in scoville:
        if x < K:
            heappush(h, x)
    
    while h:
        if len(h) == 1:
            return -1
        new = heappop(h) + heappop(h) * 2
        if new < K:
            heappush(h, new)
        cnt += 1
    return cnt
