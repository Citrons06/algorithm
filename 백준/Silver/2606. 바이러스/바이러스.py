import sys
input = sys.stdin.readline

def DFS(v):
    visited[v] = True

    for i in A[v]:
        if not visited[i]:
            DFS(i)

n = int(input())
m = int(input())

A = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

visited = [False] * (n + 1)

DFS(1)

cnt = 0
for i in range(2, n + 1):
    if visited[i]:
        cnt += 1
print(cnt)

