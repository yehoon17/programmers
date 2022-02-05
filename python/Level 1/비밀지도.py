def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        x, y = arr1[i], arr2[i]
        temp = ''
        for j in range(n):
            if x % 2 == 0 and y % 2 == 0:
                temp = ' '+temp
            else:
                temp = '#'+temp
            x //= 2
            y //= 2
        answer.append(temp)
        
    return answer
