def solution(n, words):
    s = set([words[0]])
    temp = -1
    for i in range(len(words)-1):
        if words[i][-1] == words[i+1][0]:
            if words[i+1] not in s:
                s.add(words[i+1])
            else:
                temp = i+1
                break
        else:
            temp = i+1
            break
    if temp < 0:
        return [0,0]
    else:
        return [temp%n+1,temp//n+1]
