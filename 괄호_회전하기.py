from collections import deque

def isOK(d):
    stack = []
    left = ["(", "{", "["]
    right = [")", "}", "]"]
    
    for x in d:
        for l, r in zip(left, right):
            if x == r:
                if stack and stack[-1] == l:
                    stack.pop()
                    break
            elif x == l:
                stack.append(x)
                break
        else:
            return False
    
    return not stack
                
def solution(s):
    answer = 0
    d = deque(s)
    for _ in range(len(d)):
        if isOK(d):
            answer += 1
        d.append(d.popleft())
        
    return answer
