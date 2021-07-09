def solution(arr1, arr2):
    answer=[]
    for x,y in zip(arr1, arr2):
        temp = []
        for i in range(len(x)):
            temp.append(x[i]+y[i])
        answer.append(temp)
    return answer
