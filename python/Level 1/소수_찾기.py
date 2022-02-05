def solution(n):
    temp = [1 for _ in range(n)]
    temp[0] = 0

    for i in range(2, int(n**0.5)+1):
        if temp[i-1] == 1:
            p = i
            while(True):
                p += i
                if p > n:
                    break
                temp[p-1] = 0
                
    return sum(temp)
