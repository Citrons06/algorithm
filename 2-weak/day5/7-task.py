import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

# ! 사전 작업 수 = 노드를 역으로 타고 올라갈 때 첫 노드에 도달하기 위해 거치는 노드의 수(첫 노드 포함)
def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

# 입력
n, m = map(int, input().split())

A = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    A[e].append(s)  # 역방향으로 추적하기 위해 반대로 세팅 B -> A

X = int(input())

visited = [False] * (n + 1)

DFS(X)

cnt = 0
for i in range(1, n + 1):
    if visited[i]:
        cnt += 1

print(cnt - 1)  # X 노드 제외