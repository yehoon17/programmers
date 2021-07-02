def solution(N, number):
    dp = []
    i = 1
    while(i<9):
        temp = [sum([N*(10**x) for x in range(i)])]
        if temp[0] == number:
            return i
        for j in range(i//2):
            for x in dp[j]:
                for y in dp[-1-j]:
                    if x+y == number:
                        return i
                    else:
                        temp.append(x+y)
                    if x*y == number:
                        return i
                    else:
                        temp.append(x*y)
                    large = max(x,y)
                    small = min(x,y)
                    if large - small == number:
                        return i
                    elif large>small:
                        temp.append(large - small)
                    if large % small == 0:
                        if large // small == number:
                            return i
                        else:
                            temp.append(large // small)
        dp.append(temp)
        i+=1            
    return -1
