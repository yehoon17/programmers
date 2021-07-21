def solution(stones, k):
    answer = 200001
    stones_max = stones
    for i in range(1,k):
        temp = []
        for j in range(len(stones)-i-1):
            temp.append(max(stones_max[j:j+2]))
        stones_max = temp
    return min(stones_max)
