import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    wear = defaultdict(list)
    for _ in range(n):
        wear_name, wear_class = map(str, input().split())
        wear[wear_class].append(wear_name)  # {'headgear': ['hat', 'turban'], 'eyewear': ['sunglasses']}

    cnt = 1
    # ! 각 wear_class의 아이템을 하나 씩 고르는 경우의 수 계산
    for items in wear.values():
        cnt *= (len(items) + 1)  # n개에서 1개를 고르는 경우의 수 = n + 1

    print(cnt - 1)  # 아무것도 입지 않은 경우 제외