def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for x,y in zip(A,B):
        answer+=x*y
    return answer
