import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def DFS(v):
    visited[v] = True
    is_meet = not bool(A[v])

    for i in A[v]:
        if not visited[i] and DFS(i):
            return True

    return is_meet

n, m = map(int, input().split())

A = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)

visited = [False] * (n + 1)

gom = int(input())
fans = list(map(int, input().split()))

for i in fans:
    visited[i] = True

if visited[1] or not DFS(1):
    print('Yes')
else:
    print('yes')