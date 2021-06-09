def solution(new_id):
    answer = ''
    li = []
    isStart = True
    isPeriod = False
    size = 0
    x = '~!@#$%^&*()=+[{]}:?,<>/'
    for c in new_id:
        if size > 14:
            break
        if c in x:
            continue
        if isStart:
            if c == '.':
                continue
            else:
                isStart = False
        if c == '.':
            if isPeriod:
                continue
            else:
                isPeriod = True
        else:
            isPeriod = False        
        li.append(c.lower())
        size+=1
    
    if not li:
        return 'aaa'
    
    if li[-1] == '.':
        li.pop()
        size-=1
    
    if not li:
        return 'aaa'
    
    while(size<3):
        li.append(li[-1])
        size+=1
    
    for c in li:
        answer+=c
    
    return answer
