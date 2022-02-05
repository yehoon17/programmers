from itertools import product

def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    isPuddle = [[False for _ in range(m)] for _ in range(n)]

    for x, y in puddles:
        isPuddle[y-1][x-1] = True
        
    for i, j in product(range(n), range(m)):
        if not isPuddle[i][j]:
            if i == 0 and j == 0:
                dp[i][j] = 1
            else:
                up = 0
                left = 0
                if i > 0:
                    up = dp[i-1][j]
                if j > 0:
                    left = dp[i][j-1]
                dp[i][j] = up + left

    return dp[-1][-1] % 1000000007
