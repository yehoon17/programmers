def solution(arr, divisor):
    answer = []
    arr.sort()
    for x in arr:
        if x % divisor == 0:
            answer.append(x)
    if answer:
        return answer
        
    return [-1]
