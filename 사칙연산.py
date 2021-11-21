from collections import deque

def max_result(arr):
    if not arr:
        return 0
    
    result = 0
    while arr:
        x = arr.popleft()
        if x == "-":
            break
        elif not x == "+":
            result += int(x)
    return result - min_result(arr)

def min_result(arr):
    if not arr:
        return 0
    
    result = 0
    while arr:
        x = arr.popleft()
        if x == "-":
            break
        elif not x == "+":
            result += int(x)
    return result - max_result(arr)

def solution(arr):
    arr = deque(arr)
    return max_result(arr)
