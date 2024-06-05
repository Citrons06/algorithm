import sys
input = sys.stdin.readline

n = int(input())
m = [int(input()) for _ in range(n)]

max_bar = m[-1]
cnt = 1

for i in range(n-2, -1, -1):
    if max_bar < m[i]:
        cnt += 1
        max_bar = m[i]

print(cnt)
