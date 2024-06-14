n = int(input())
milks = list(map(int, input().split()))
drinking = [0, 1, 2]

cnt = 0
idx = 0
for milk in milks:
    if milk == drinking[idx % 3]:
        cnt += 1
        idx += 1

print(cnt)