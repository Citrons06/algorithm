import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def DFS(v):
    visited[v] = True
    is_meet = not bool(A[v])  # 자식이 없는 노드인지 확인

    for i in A[v]:
        # 자식이 없는 노드에 끝까지 도달하면 True
        if not visited[i] and DFS(i):
            return True

    return is_meet

# 입력
n, m = map(int, input().split())  # n: 노드, m: 간선의 수

A = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)

visited = [False] * (n + 1)

gom = int(input())
fans = list(map(int, input().split()))  # 팬 노드 번호

# 팬이 있는 노드를 방문한 것으로 표시 -> DFS() 에서 팬이 있는 노드까지 도달하면 STOP
for i in fans:
    visited[i] = True

if visited[1] or not DFS(1):
    print('Yes')
else:
    print('yes')