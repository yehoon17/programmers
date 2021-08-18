def solution(n, money):
    dp = [0 for _ in range(n+1)]
    dp[-1] = 1
    for x in money:
        for i in range(n,-1,-1):
            if i<x:
                break
            dp[i-x]+=dp[i]
            i-=x
    return dp[0]%1000000007
