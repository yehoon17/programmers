def solution(n, k):
    answer = []

    fact = [1]
    for i in range(1, n):
        fact.append(fact[-1]*i)

    nums = [False for _ in range(n+1)]

    for m in range(n):
        d = fact[n-1-m]
        q, r = (k-1) // d, k % d
        if r == 0:
            r = d
        k = r
        for i in range(1, 1+n):
            if not nums[i]:
                q -= 1
            if q < 0:
                if not nums[i]:
                    answer.append(i)
                    nums[i] = True
                    break

    return answer
