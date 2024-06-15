def paint(n, color):
    dp = [[0] * 3 for _ in range(n)]

    dp[0][0] = color[0][0]
    dp[0][1] = color[0][1]
    dp[0][2] = color[0][2]

    for i in range(1, n):
        dp[i][0] = color[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = color[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = color[i][2] + min(dp[i-1][0], dp[i-1][1])
    return min(dp[n-1][0], dp[n-1][1], dp[n-1][2])


n = int(input())

color = []
for _ in range(n):
    color.append(list(map(int, input().split())))

print(paint(n, color))