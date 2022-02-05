def solution(prices):
    answer = []
    size = len(prices)
    for i in range(size):
        temp = 0
        for j in range(i+1, size):
            temp += 1
            if prices[i] > prices[j]:
                break
    
        answer.append(temp)

    return answer
