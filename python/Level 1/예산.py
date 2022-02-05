def solution(d, budget):
    d.sort()
    answer = 0
    
    for x in d:
        if budget >= x:
            budget -= x
            answer += 1
        else:
            break
        
    return answer
