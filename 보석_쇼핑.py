def solution(gems):
    size = len(gems)
    answer = [0, size]
    index_of = {}
    total = len(set(gems))
    min_gem = gems[0]
    for i, gem in enumerate(gems):
        index_of[gem] = i
        if min_gem == gem:
            min_gem = min(index_of, key=lambda x: index_of[x])
        if len(index_of) == total:
            start = index_of[min_gem]
            end = i
            if answer[1] - answer[0] > end - start:
                answer = [start+1, end+1]
                
    return answer
