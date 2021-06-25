def solution(s):
    answer=''
    isStart=True
    for c in s:
        if c in (' ','\t','\n'):
            isStart=True
        else:
            if isStart:
                isStart=False
                c=c.upper()
            else:
                c=c.lower()
        answer+=c
    return answer
