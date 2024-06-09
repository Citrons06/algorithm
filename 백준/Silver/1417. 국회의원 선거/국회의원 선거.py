n = int(input())
dasom = int(input())
candidates = [int(input()) for _ in range(n-1)]

cnt = 0
if n == 1:
    pass
else:
    while max(candidates) >= dasom:
        dasom += 1
        candidates[candidates.index(max(candidates))] -= 1
        cnt += 1

print(cnt)