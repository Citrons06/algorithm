def tiling(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    # dp[i] = 가로 i 길이의 직사각형에 두 종류의 타일을 채우는 경우의 수
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

    return dp[n]

n = int(input())
print(tiling(n))