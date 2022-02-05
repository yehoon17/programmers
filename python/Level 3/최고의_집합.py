def solution(n, s):
    if n > s:
        return [-1]

    temp = s // n
    answer = [temp for _ in range(n)]
    for i in range(s%n):
        answer[-i-1] += 1

    return answer
