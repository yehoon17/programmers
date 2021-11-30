def solution(gems):
    size = len(gems)
    answer = [0, size]
    index_of = {}
    total = len(set(gems))
    # start = size
    # end = -1
    for i, gem in enumerate(gems):
        index_of[gem] = i
        if len(index_of) == total:
            start = min(index_of.values())
            end = i
            if answer[1] - answer[0] > end - start:
                answer = [start+1, end+1]
                
    return answer
