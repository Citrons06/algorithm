# dp 테이블로 1 ~ 10 까지의 값 계산
def sum_case(n):
    dp = [0] * (n + 1)
    dp[0] = 1  # 0일 때 연산 불필요

    # dp[i] = i를 1, 2, 3의 합으로 나타낼 수 있는 경우의 수
    for i in range(1, n + 1):
        if i >= 1:
            dp[i] += dp[i - 1]

        if i >= 2:
            dp[i] += dp[i - 2]

        if i >= 3:
            dp[i] += dp[i - 3]

    return dp[n]

t = int(input())

for _ in range(t):
    n = int(input())
    print(sum_case(n))