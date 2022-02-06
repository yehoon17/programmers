def solution(n):
    answer = 0
    s = str(n)
    for x in s:
        answer += int(x)
    return answer
