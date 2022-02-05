def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        x = []
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr1[0])):
                temp += arr1[i][k] * arr2[k][j]
            x.append(temp)
        answer.append(x)

    return answer
