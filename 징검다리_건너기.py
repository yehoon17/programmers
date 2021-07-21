def solution(stones, k):
    answer = 200001
    for i in range(len(stones)-k):
        if answer>max(stones[i:i+k]):
            answer=max(stones[i:i+k])
    return answer
