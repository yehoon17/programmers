def solution(absolutes, signs):
    answer = 0
    for n, sign in zip(absolutes, signs):
        if sign:
            answer += n
        else:
            answer -= n
            
    return answer
