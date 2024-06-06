from collections import deque

n, m, v = map(int, input().split())  # n: 노드 개수, m: 에지 개수, v: 시작점
A = [[] for _ in range(n + 1)]  # 그래프 데이터 저장 리스트

for i in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(n + 1):
    A[i].sort()  # 번호가 작은 노드부터 방문하기 위해 정렬

def DFS(now):
    print(now, end=' ')  # 현재 노드 출력
    visited[now] = True  # 방문 리스트에 현재 노드 체크

    # 현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS 실행
    for i in A[now]:
        if not visited[i]:
            DFS(i)

visited = [False] * (n + 1)
DFS(v)

def BFS(now):
    que = deque()
    que.append(now)  # 시작 노드 삽입
    visited[now] = True  # 방문 리스트에 현재 노드 체크

    while que:  # 큐가 비어 있을 때까지
        now_node = que.popleft()
        print(now_node, end=' ')

        # 현재 노드의 연결 노드 중 방문하지 않은 노드 append
        # 방문리스트에 체크
        for i in A[now_node]:
            if not visited[i]:
                que.append(i)
                visited[i] = True

print()
visited = [False] * (n + 1)
BFS(v)


