def solution(numbers):
    answer = ''
    size = len(numbers)
    for i in range(size):
        max_index = i
        for j in range(i+1, size):
            a = numbers[max_index]
            b = numbers[j]
            if a < 10:
                len_a = 1
            elif a < 100:
                len_a = 2
            elif a < 1000:
                len_a = 3
            else:
                len_a = 4
            if b < 10:
                len_b = 1
            elif a < 100:
                len_b = 2
            elif a < 1000:
                len_b = 3
            else:
                len_b = 4
            if a*(10**len_b)+b < b*(10**len_a)+a:
                max_index = j
        numbers[max_index], numbers[i] = numbers[i], numbers[max_index]
        answer+=str(numbers[i])
    return str(int(answer))
