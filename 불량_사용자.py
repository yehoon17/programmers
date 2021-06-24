def solution(user_id, banned_id):
    answer = 0
    dic={}
    for x in banned_id:
        dic[x]=[]
        for y in user_id:
            if len(x) == len(y):
                isMatch = True
                for a,b in zip(x,y):
                    if a == '*' or a==b:
                        pass
                    else:
                        isMatch = False
                        break
                if isMatch:
                    dic[x].append(y)
                    
    
                        
    return answer
