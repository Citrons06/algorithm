import sys

sys.setrecursionlimit(200000)
input = sys.stdin.readline

def DFS(idx, order):
    global now_order
    visited[idx] = now_order
    now_order += 1

    for i in A[idx]:
        if visited[i] == 0:
            DFS(i, now_order)

# 입력
n, m, r = map(int, input().split())  # 정점의 수, 간선의 수, 시작 정점
A = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(1, n + 1):
    A[i].sort()

visited = [0] * (n + 1)

now_order = 1
DFS(r, now_order)

for i in range(1, n + 1):
    print(visited[i])