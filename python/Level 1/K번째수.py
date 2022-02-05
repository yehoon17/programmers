def solution(array, commands):
    answer = []
    
    for start, end, order in commands:
        temp = array[start-1:end]
        temp.sort()
        answer.append(temp[order-1])

    return answer
