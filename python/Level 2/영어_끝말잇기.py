def solution(n, words):
    vocab = set([words[0]])
    temp = -1
    for i in range(len(words)-1):
        if words[i][-1] == words[i+1][0] and words[i+1] not in vocab:
            vocab.add(words[i+1])
        else:
            temp = i + 1
            break

    if temp < 0:
        return [0, 0]
    else:
        return [temp % n+1, temp//n+1]
