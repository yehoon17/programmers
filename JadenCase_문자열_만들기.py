def solution(s):
    answer=''
    isStart=True
    for c in s:
        if isStart:
            isStart=False
            c=c.upper()
        else:
            if c in (' ','\t','\n'):
                isStart=True
            else:
                c=c.lower()
        answer+=c
    return answer
