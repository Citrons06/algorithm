import sys
input = sys.stdin.readline

# ! 촌수 계산하는 사람부터 탐색해도 될 듯 -> found: True, False

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

# 입력
n = int(input())
x, y = map(int, input().split())  # 촌수를 계산해야 하는 두 사람

m = int(input())

A = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

visited = [False] * (n + 1)
found = False

DFS(x, 0)  # 촌수를 계산하는 사람부터 탐색

# 계산할 수 없으면(found = False) -1 출력
if not found:
    print(-1)