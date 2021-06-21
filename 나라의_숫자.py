def solution(n):
    answer = ''
    while(n>0):
        digit = 2**((n-1)%3)
        n=(n-1)//3
        answer = str(digit)+answer
    return answer
