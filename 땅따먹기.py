def solution(land):
    land.append([0,0,0,0])
    for i,l in enumerate(land):
        for j in range(4):
            l[j] += max([land[i-1][-k+j] for k in range(1,4)])
    return max(land[-2])
