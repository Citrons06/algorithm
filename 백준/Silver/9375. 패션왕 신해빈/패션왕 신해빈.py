import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    wear = defaultdict(list)
    for _ in range(n):
        wear_name, wear_class = map(str, input().split())
        wear[wear_class].append(wear_name)
    cnt = 1
    for items in wear.values():
        cnt *= (len(items) + 1)

    print(cnt - 1)


