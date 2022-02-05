def solution(N, stages):
    temp = [0 for _ in range(N+1)]
    for s in stages:
        temp[s-1] += 1
        
    size = len(stages)
    fail_rate = [0 for _ in range(N)]
    for i in range(N):
        fail_rate[i] = temp[i]/size
        size -= temp[i]
        if size == 0:
            break

    answer = list(range(1, N+1))
    answer.sort(key=lambda x: fail_rate[x-1], reverse=True)

    return answer
