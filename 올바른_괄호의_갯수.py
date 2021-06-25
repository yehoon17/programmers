def solution(n):
    dp=[1,1]
    for i in range(1,n):
        temp = 0
        for j in range(i+1):
            print(j)
            temp+=dp[j]*dp[-1-j]
        dp.append(temp)
    return dp[-1]
            
