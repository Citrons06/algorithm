import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())  # 노드, 에지 개수
visited = [False] * (n + 1)  # 방문 여부 리스트
arrive = False  # 깊이==5의 여부
A = [[] for _ in range(n + 1)]  # 에지-노드 저장 리스트

def DFS(now, depth):
    global arrive

    # 깊이가 5가 되면 바로 종료
    if depth == 5:
        arrive = True
        return

    # 현재 노드를 방문 리스트에 체크
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            DFS(i, depth + 1)

    visited[now] = False

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(n):
    DFS(i, 1)
    if arrive:
        break

print(1) if arrive else print(0)