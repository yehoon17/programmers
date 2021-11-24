def solution(stones, k):
    answer = max(stones[:k])
    for i in range(len(stones)-k):
        answer = min(max(stones[i:i+k]), answer)
    return answer
