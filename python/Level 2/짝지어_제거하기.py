def solution(s):
    l = list(s)
    while l:
        temp = []
        isNew = False
        for c in l:
            if temp and temp[-1] == c:
                isNew = True
                temp.pop()
            else:
                temp.append(c)

        if isNew:
            l = temp
        else:
            return 0

    return 1
