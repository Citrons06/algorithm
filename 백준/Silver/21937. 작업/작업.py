import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

n, m = map(int, input().split())

A = [[] for _ in range(n + 1)]
for _ in range(m):
    a_task, b_task = map(int, input().split())
    A[b_task].append(a_task)

X = int(input())

visited = [False] * (n + 1)

DFS(X)

cnt = 0
for i in range(1, n + 1):
    if visited[i]:
        cnt += 1

print(cnt - 1)