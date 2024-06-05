from itertools import combinations

n, m = map(int, input().split())
list = []

for i in range(1, n+1):
    list.append(i)

# combinations 사용해서 m개를 고르는 모든 조합 뽑기
a = combinations(list, m)
for i in a:
    print(*i)

# 31120KB 40ms