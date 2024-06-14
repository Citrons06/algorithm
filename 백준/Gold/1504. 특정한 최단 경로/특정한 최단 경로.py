import sys
from heapq import heappop, heappush

input = sys.stdin.readline

# 두 개의 경우의 수: 1 -> v1 -> v2 -> n / 1 -> v2 -> v1 -> n
# 이 중 최단거리 찾아야 함

# start에서 다른 모든 정점으로의 최단 거리 계산
def dijkstra(start):
    dist = [INF] * (n + 1)  # 각 정점까지의 최단거리 저장
    dist[start] = 0
    queue = [(0, start)]

    # 큐에서 가장 짧은 거리의 정점을 꺼내서 인접한 정점들로의 거리 갱신
    while queue:
        cost, u = heappop(queue)
        if dist[u] < cost:
            continue

        for adj, d in A[u]:
            if dist[adj] > cost + d:
                dist[adj] = cost + d
                heappush(queue, (dist[adj], adj))  # 거리 갱신

    return dist

INF = float('inf')  # 초기 거리 값을 무한대로 세팅

n, m = map(int, input().split())  # 정점의 개수, 간선의 개수

A = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())  # a, b: 정점, c: 거리
    A[a].append((b, c))
    A[b].append((a, c))

v1, v2 = map(int, input().split())  # 반드시 거쳐야 하는 정점

dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)  # v1에서 시작
dist_from_v2 = dijkstra(v2)  # v2에서 시작

# v1_route: 1 -> v1 -> v2 -> n
# v2_route: 1 -> v2 -> v1 -> n
v1_route = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]
v2_route = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]

min_route = min(v1_route, v2_route)

# 찾은 경로가 무한대면 연결된 경로가 없음을 의미
if min_route >= INF:
    print(-1)
else:
    print(min_route)