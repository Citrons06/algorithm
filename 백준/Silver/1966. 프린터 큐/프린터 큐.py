import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    imp = deque(list(map(int, input().split())))

    doc = deque([i for i in range(n)])
    cnt = 0

    while doc:
        if imp[0] == max(imp):
            cnt += 1
            imp.popleft()
            if doc.popleft() == m:
                print(cnt)
                break
        else:
            imp.append(imp.popleft())
            doc.append(doc.popleft())