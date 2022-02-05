from collections import deque
from itertools import islice

def dq_slice(arr, start):
    return deque(islice(arr, start, len(arr)))

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
    if arr:
        result0 = result - int(arr[0]) + max_result(dq_slice(arr, 1))
        result1 = result - min_result(arr)
        return max(result0, result1)
    else:
        return result

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
    if arr:
        result0 = result - int(arr[0]) + min_result(dq_slice(arr, 1))
        result1 = result - max_result(arr)
        return min(result0, result1)
    else:
        return result

def solution(arr):
    arr = deque(arr)
    return max_result(arr)
