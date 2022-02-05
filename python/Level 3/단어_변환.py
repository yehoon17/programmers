def isTran(word1, word2):
    count = 0
    for c1, c2 in zip(word1, word2):
        if not c1 == c2:
            count += 1
            if count > 1:
                return False
    if count == 0:
        return False
    return True


def dfs(begin, target, words, visited):
    if begin == target:
        return 0
    visited[begin] = True
    temp = len(words)+1
    for word in words:
        if not visited[word]:
            if isTran(begin, word):
                temp = min(temp, dfs(word, target, words, visited) + 1)
    visited[begin] = False
    return temp


def solution(begin, target, words):
    if target not in words:
        return 0
    visited = {word: False for word in words}
    answer = dfs(begin, target, words, visited)
    if answer > len(words):
        return 0
    return answer
