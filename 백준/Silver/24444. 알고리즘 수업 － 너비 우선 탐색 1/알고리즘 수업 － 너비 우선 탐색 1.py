from collections import deque
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def BFS(idx):
    queue = deque()
    queue.append(idx)

    visited[idx] = 1
    order = 2

    while queue:
        now_node = queue.popleft()

        for i in A[now_node]:
            if visited[i] == 0:
                visited[i] = order
                order += 1
                queue.append(i)

n, m, r = map(int, input().split())
A = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(1, n+1):
    A[i].sort()

visited = [0] * (n + 1)

BFS(r)

for i in range(1, n+1):
    print(visited[i])