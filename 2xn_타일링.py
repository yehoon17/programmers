def solution(n):
    dp = [1,2]
    for _ in range(n-2):
        dp.append(dp[-1]+dp[-2])
    return dp[n-1]%1000000007
