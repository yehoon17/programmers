def solution(user_id, banned_id):
    cases = []
    for x in banned_id:
        candidate=[]
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
                    candidate.append(y)
        if not cases:
            cases = [set([id_]) for id_ in candidate]
        else:
            temp = []
            for case in cases:
                for id_ in candidate:
                    if id_ not in case:
                        new_case = case|set([id_])
                        if new_case not in temp:
                            temp.append(new_case)
            cases = temp
    return len(cases)
