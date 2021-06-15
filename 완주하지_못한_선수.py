def solution(participant, completion):
    d = {}
    for c in completion:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    for p in participant:
        if p not in d:
            return p
        d[p] -= 1
        if d[p] < 0:
            return p
