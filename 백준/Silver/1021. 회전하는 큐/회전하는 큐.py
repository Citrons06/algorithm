from collections import deque

n, m = map(int, input().split())
loc = list(map(int, input().split()))
que = deque([i for i in range(1, n+1)])

cnt = 0
for target in loc:
    while True:
        if que[0] == target:
            que.popleft()
            break
        else:
            if que.index(target) <= len(que) // 2:
                que.rotate(-1)
                cnt += 1
            if que.index(target) >= len(que) // 2:
                que.rotate(1)
                cnt += 1

print(cnt)