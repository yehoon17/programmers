from collections import deque

def solution(stones, k):
    answer = 200000001
    k_window = deque()
    
    for i, stone in enumerate(stones):
        while k_window and stones[k_window[-1]] <= stone:
            k_window.pop()
        k_window.append(i)
        if k_window[0] == i - k:
            k_window.popleft()
        if i >= k - 1:
            answer = min(answer, stones[k_window[0]])
    return answer
