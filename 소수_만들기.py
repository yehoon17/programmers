from itertools import combinations

def solution(nums):
    prime = [True for _ in range(3000)]
    n = 2
    while(True):
        if prime[n]:
            for k in range(2,3000//n):
                prime[k*n]=False
        n+=1
        if n>2999:
            break
    answer = 0
    for a,b,c in combinations(nums,3):
        n = a+b+c
        if prime[n]:
            answer+=1
    return answer
