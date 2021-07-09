def solution(n, k, cmd):
    exists = [True for _ in range(n)]
    stack = []
    i = k
    for c in cmd:
        if c == 'C':
            exists[i] = False
            stack.append(i)
        elif c == 'Z':
            exists[stack.pop()] = True
        else:
            x,y = c.split()
            z = int(y)
            if x == 'D':
                while(z>0):
                    if exists[i]:
                        z-=1
                    i+=1    
            elif x == 'U':
                while(z>0):
                    if exists[i]:
                        z-=1
                    i-=1 
    answer=''
    for x in exists:
        if x:
            answer+='O'
        else:
            answer+='X'
    return answer
                
