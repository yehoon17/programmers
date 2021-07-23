def solution(n, money):
    answer = 0
    money.sort(reverse=True)
    c = money.pop()
    dp = [n]
    for x in money:
        temp = []
        for y in dp:
            z = y
            while(z>0):
                temp.append(z)
                z-=x
                if z == 0:
                    answer+=1
        dp = temp
        
    for y in dp:
        if y%c == 0:
            answer+=1
    
    return answer%1000000007
