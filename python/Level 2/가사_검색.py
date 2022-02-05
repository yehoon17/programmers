def match(query, word):
    if len(query) == len(word):
        for i in range(len(word)):
            if query[i] == "?":
                pass
            else:
                if not query[i] == word[i]:
                    return False
        return True
    return False


def solution(words, queries):
    answer = []
    for query in queries:
        cnt = 0
        for word in words:
            if match(query, word):
                cnt += 1
        answer.append(cnt)
    return answer
