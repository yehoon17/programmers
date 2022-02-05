def solution(n):
    if n % 2 == 1:
        return 0
    n = n // 2 - 1
    dp = [3]
    for _ in range(n):
        temp = 3*dp[-1] + 2*sum(dp[:-1]) + 2
        dp.append(temp)
    return dp[n] % 1000000007
