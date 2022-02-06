def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(1 + max(i // n, i % n))

    return answer
