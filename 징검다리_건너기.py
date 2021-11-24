from collections import deque

def solution(stones, k):
    tmp = deque()
    
    for _ in range(k):
        tmp.append(stones.pop())
        
    answer = max(tmp)
    while stones:
        tmp.append(stones.pop())
        tmp.popleft()
        answer = min(max(tmp), answer)
        
    return answer
