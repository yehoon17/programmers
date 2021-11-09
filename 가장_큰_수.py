def expend(num):
    if num == "0":
        return 0
    
    num = int(num)
    zero = 1
    while num % 10 == 0:
        num //= 10
        zero += 1
    
    num *= 10 ** (4 - len(str(num)))
    num -= zero
    
    return num

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=expend)
        
    return str(int("".join(numbers)))
