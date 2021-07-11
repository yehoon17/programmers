def solution(places):
    answer = []
    for place in places:
        isValid = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if i<3:
                        if place[i+1][j] == 'O' and place[i+2][j] == 'P':
                            answer.append(0)
                            isValid = False
                            break
                    if j<3:
                        if place[i][j+1] == 'O' and place[i][j+2] == 'P':
                            answer.append(0)
                            isValid = False
                            break
                    if i<4 and j<4:
                        if place[i+1][j] == 'O' or place[i][j+1] == 'O':
                            if place[i+1][j+1] == 'P':
                                answer.append(0)
                                isValid = False
                                break   
            if not isValid:
                break
        if isValid:
            answer.append(1)
                                
                            
    return answer
