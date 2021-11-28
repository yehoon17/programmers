from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for p in permutations(dungeons):
        cnt = 0
        k_remain = k
        for threshold, cost in p:
            if k_remain >= threshold:
                k_remain -= cost
                cnt += 1
        answer = max(answer, cnt)
    return answer
