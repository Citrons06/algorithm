import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def BFS(start):

    queue = deque([start])
    distances[start] = 0  # 시작 도시 거리=0

    while queue:
        now_city = queue.popleft()

        # 현재 갈 수 있는 도시 중 방문하지 않았던 도시의 거리 = 현재 도시의 거리 + 1
        # distances 리스트에 세팅
        for next_city in A[now_city]:
            if distances[next_city] == -1:
                distances[next_city] = distances[now_city] + 1
                queue.append(next_city)

# 입력

# n: 노드, m: 간선, k: 거리, x: 출발 번호
n, m, k, start_city = map(int, input().split())

A = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    A[a].append(b)  # a -> b 단방향

# ! 도시의 최단 거리를 모두 -1로 세팅
distances = [-1] * (n + 1)

BFS(start_city)

ans = []
for city in range(1, n+1):
    if distances[city] == k:
        ans.append(city)

if ans:
    ans.sort()
    for city in ans:
        print(city)
else:
    print(-1)