def sugar(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + 1)
        if i >= 5:
            dp[i] = min(dp[i], dp[i - 5] + 1)

    if dp[n] == float('inf'):
        return -1
    else:
        return dp[n]

n = int(input())
print(sugar(n))