def solution(begin, end):
    answer = []
    if begin == 1:
        answer.append(0)
        begin += 1
    
    for i in range(begin, end + 1):
        isPrime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0 and i // j < 10000000:
                answer.append(i // j)
                isPrime = False
                break
        if isPrime:
            answer.append(1)
    return answer
