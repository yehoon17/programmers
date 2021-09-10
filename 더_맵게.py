from heapq import heappush, heappop

def solution(scoville, K):
    cnt = 0
    h = []
    for x in scoville:
        heappush(h, x)
    
    while h[0] < K:
        if len(h) == 1:
            return -1
        new = heappop(h) + heappop(h) * 2
        heappush(h, new)
        cnt += 1
        
    return cnt
