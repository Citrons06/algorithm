n, k = map(int, input().split())  # 동전의 종류 개수, 목표 액수

coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)  # 최적의 경우를 찾기 위해 내림차순 정렬

cnt = 0
for i in range(n):
    if coins[i] <= k:
        cnt += k // coins[i]
        k %= coins[i]

print(cnt)