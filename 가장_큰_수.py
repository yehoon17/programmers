def expend(num):
    num = num + num[-1] * (4 - len(num))
    
    return num

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=expend)
        
    return str(int("".join(numbers)))
