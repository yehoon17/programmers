from itertools import permutations

def solution(numbers):
    answer = 0
    primes = set()
    for n in range(1,len(numbers)+1):
        for p in permutations(numbers,n):
            numstr = ''
            for i in p:
                numstr+=i
            num = int(numstr)
            isPrime = True
            for d in range(2,int(num**0.5)+1):
                if num%d==0:
                    isPrime = False
                    break
            if isPrime and num>1:
                if num not in primes:
                    answer+=1
                    primes.add(num)
    return answer
