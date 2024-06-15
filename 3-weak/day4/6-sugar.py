def sugar(n):
    dp = [float('inf')] * (n + 1) # 0이 아니라 무한대로 세팅해야 함,,
    dp[0] = 0

    # dp[i] = i킬로그램의 설탕을 가져갈 수 있는 봉지의 최솟값
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