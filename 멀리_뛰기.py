def solution(n):
    dp=[1,2]
    for i in range(2,n):
        dp.append((dp[-1]+dp[-2])%1234567)
    return dp[n-1]
