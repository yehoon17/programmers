def solution(number, k):
    answer = ''
    start = 0
    while k > 0:
        if len(number)-start == k:
            return answer

        max = '0'
        for i in range(start, start+k+1):
            if max < number[i]:
                max = number[i]
                index = i
                if max == '9':
                    break

        answer += max
        k -= index - start
        start = index+1
        
    answer += number[start:]

    return answer
