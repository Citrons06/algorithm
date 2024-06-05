import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())  # 노드, 에지의 개수
A = [[] for _ in range(n+1)] # 그래프 데이터 저장 인접 리스트
visit = [False] * (n + 1) # 방문 기록 리스트

# DFS
def DFS(v):
    visit[v] = True
    for i in A[v]:
        if not visit[i]:
            DFS(i)

for _ in range(m):
    s, e = map(int, input().split())  # 에지의 양끝 점
    A[s].append(e)  # 양방향 에지이므로 양쪽에 에지를 더함
    A[e].append(s)

cnt = 0

for i in range(1, n+1):
    if not visit[i]:  # 방문하지 않았던 노드 탐색
        cnt += 1
        DFS(i)

print(cnt)