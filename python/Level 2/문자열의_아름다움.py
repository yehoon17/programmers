def beauty(s, dp, i, k):
    j = i + k

    if s[i] != s[j]:
        return j - i
    else:
        return max(dp[i], dp[i+1])

def solution(s):
    answer = 0
    size = len(s)
    dp = [0 for _ in range(size)]
    for k in range(1, size):
        new_dp = []
        for i in range(size-k):
            new_dp.append(beauty(s, dp, i, k))
        dp = new_dp
        answer += sum(dp)
    return answer
