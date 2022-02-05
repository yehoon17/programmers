def solution(s):
    l = list(map(int, s.split()))
    return str(min(l)) + ' ' + str(max(l))
