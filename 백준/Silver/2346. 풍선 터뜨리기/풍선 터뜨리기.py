import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
b = deque(list(enumerate((map(int, input().split())), start=1)))
ans = []

while b:
    idx, num = b.popleft()
    ans.append(idx)

    if num > 0:
        b.rotate(-(num - 1))
    if num < 0:
        b.rotate(-num)

print(*ans)