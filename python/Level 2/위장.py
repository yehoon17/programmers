from itertools import combinations


def solution(clothes):
    answer = 1
    cnt = {}
    for _, type_ in clothes:
        if type_ in cnt:
            cnt[type_] += 1
        else:
            cnt[type_] = 1

    l = list(cnt.values())
    for i in l:
        answer *= i + 1

    return answer - 1
