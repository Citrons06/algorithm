import sys
input = sys.stdin.readline

def DFS(v, rel_cnt):
    global found

    if v == y:
        print(rel_cnt)
        found = True
        return

    visited[v] = True
    for i in A[v]:
        if not visited[i] and not found:
            DFS(i, rel_cnt + 1)

n = int(input())
x, y = map(int, input().split())
m = int(input())
A = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)
visited = [False] * (n + 1)
found = False

DFS(x, 0)

if not found:
    print(-1)