def solution(n, cores):
    answer = 0
    size = len(cores)
    temp = [0]*size
    while(n>0):
        for i in range(size):
            if temp[i] == 0:
                temp[i] = cores[i]
                n-=1
                if n == 0:
                    return i+1
            temp[i]-=1
