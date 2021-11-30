def solution(gems):
    answer = [0, len(gems)]
    index_of = {}
    total = len(set(gems))
    for i, gem in enumerate(gems):
        index_of[gem] = i
        if len(index_of) == total:
            start = min(index_of.values())
            end = max(index_of.values())
            if answer[1] - answer[0] > end - start:
                answer = [start+1, end+1]
                
    return answer
