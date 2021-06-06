from itertools import combinations

def solution(clothes):
    answer = 1
    d = {}
    for item, key in clothes:
        if key in d:
            d[key]+=1
        else:
            d[key]=1
    l = list(d.values())
    for i in l:
        answer*=i+1
    return answer-1
