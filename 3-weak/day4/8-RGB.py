def paint(n, color):
    dp = [[0] * 3 for _ in range(n)]

    # 첫 번째 집 색칠 비용
    dp[0][0] = color[0][0]
    dp[0][1] = color[0][1]
    dp[0][2] = color[0][2]

    # dp[i] = i 개의 집을 이전 집과 중복되지 않게 칠하는 경우의 최소 비용
    # i 번째 집을 빨강으로 칠하는 최소 비용 = i-1 번째 집을 초, 파랑으로 칠하는 최소비용 + i 번째 집을 빨강으로 칠하는 비용
    for i in range(1, n):
        dp[i][0] = color[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = color[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = color[i][2] + min(dp[i-1][0], dp[i-1][1])

    # 마지막 집까지 칠하는 최소 비용
    return min(dp[n-1][0], dp[n-1][1], dp[n-1][2])

n = int(input())

color = []
for _ in range(n):
    color.append(list(map(int, input().split())))

print(paint(n, color))