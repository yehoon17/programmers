def solution(begin, end):
    answer = []
    isPrime = [True for _ in range(1+min(end,10000000))]
    primes = []
    i=2
    while(True):
        if i>len(isPrime)-1:
            break
        if isPrime[i]:
            primes.append(i)
            temp = i
            while(True):
                temp+=i
                if temp>len(isPrime)-1:
                    break
                isPrime[temp]=False
        i+=1
    for i in range(begin,end+1):
        if i==1 or i>10000000:
            answer.append(0)
            continue
        if i in primes:
            answer.append(1)
        else:
            for p in primes:
                if i%p==0:
                    answer.append(i//p)
                    break
    return answer
