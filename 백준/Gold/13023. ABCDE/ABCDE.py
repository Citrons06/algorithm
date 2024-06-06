import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())  # 노드, 에지 개수
A = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)
arrive = False

def DFS(now, depth):
    global arrive

    if depth == 5:  # 깊이가 5가 되면 종료
        arrive = True
        return
    visit[now] = True

    for i in A[now]:
        if not visit[i]:  # 방문 여부 체크
            DFS(i, depth + 1)  # 재귀 호출마다 깊이 증가
    visit[now] = False

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)  # 양쪽에 에지 더하기
    A[e].append(s)

for i in range(n):
    DFS(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)