def min_coin(coins, change, pay):
    cnt = 0

    change = change - pay
    for coin in coins:
        if change == 0:
            break

        cnt += change // coin
        change %= coin

    return cnt

n = int(input())
coins = [500, 100, 50, 10, 5, 1]
amount = 1000

print(min_coin(coins, amount, n))
