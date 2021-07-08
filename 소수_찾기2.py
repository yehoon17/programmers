from itertools import permutations

def solution(numbers):
    answer = 0
    for p in set(permutations(numbers)):
        numstr = ''
        for i in p:
            numstr+=i
        num = int(numstr)
        isPrime = True
        for d in range(2,int(num**0.5)+1):
            if num%d==0:
                isPrime = False
                break
        if isPrime:
            answer+=1
    return answer
