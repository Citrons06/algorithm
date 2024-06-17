n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

cnt = 0
for i in range(n):
    if coins[i] <= k:
        cnt += k // coins[i]
        k %= coins[i]

print(cnt)