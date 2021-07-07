def solution(begin, end):
    answer = [0 for _ in range(begin,end+1)]
    for i in range(1,end):
        if i>10000000:
            break
        for j in range(begin,end+1):
            if j>10000000:
                break
            if j%i==0 and j>i:
                answer[j-begin]=i
    return answer
        
