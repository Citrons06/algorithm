from itertools import combinations

# 수열의 모든 조합 뽑고 sum == m 인 조합 찾을 때마다 cnt++

n, m = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(1, n + 1):

    for a in combinations(A, i):
        if sum(a) == m:
            cnt += 1

print(cnt)