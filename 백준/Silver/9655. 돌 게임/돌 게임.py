def stone_game(n):
    dp = [False] * (n + 1)
    dp[0] = False

    for i in range(1, n + 1):
        if i - 1 >= 0 and not dp[i - 1]:
            dp[i] = True

        elif i - 3 >= 0 and not dp[i - 1]:
            dp[i] = True

        else:
            dp[i] = False

    return dp[n]


n = int(input())

if stone_game(n):
    print('SK')
else:
    print('CY')
