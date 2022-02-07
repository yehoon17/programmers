def solution(x):
    if x % sum(map(int, str(x))) == 0:
        return True
    
    return False
