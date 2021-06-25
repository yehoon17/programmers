def solution(n):
    prime = []
    for i in range(2,n+1):
        isPrime=True
        for p in prime:
            if i%p==0:
                isPrime=False
                break
        if isPrime:
            prime.append(i)
    return len(prime)
