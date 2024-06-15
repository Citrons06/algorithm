def stone_game(n):
    dp = [False] * (n + 1)
    dp[0] = False

    # i-1, i-3개 남았을 때 창영이가 지면 상근이가 이김
    # True: 상근(승) False: 창영(승)
    for i in range(1, n + 1):

        # 상근이가 이길 수 있는지 확인
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
