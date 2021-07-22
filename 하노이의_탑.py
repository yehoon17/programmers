def move(n,start,end):
    if n == 1:
        return [[start,end]]
    else:
        empty = ({1,2,3} - {start,end}).pop()
        return move(n-1,start,empty) + [[start,end]] + move(n-1,empty,end)

def solution(n):
    return move(n,1,3)
