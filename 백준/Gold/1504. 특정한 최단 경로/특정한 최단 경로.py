from heapq import heappop, heappush

def dijkstra(start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    queue = [(0, start)]

    while queue:
        cost, u = heappop(queue)
        if dist[u] < cost:
            continue

        for adj, d in A[u]:
            if dist[adj] > cost + d:
                dist[adj] = cost + d
                heappush(queue, (dist[adj], adj))

    return dist

INF = float('inf')

n, m = map(int, input().split())

A = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    A[a].append((b, c))
    A[b].append((a, c))

v1, v2 = map(int, input().split())

dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

v1_route = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]
v2_route = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]

min_route = min(v1_route, v2_route)

if min_route >= INF:
    print(-1)
else:
    print(min_route)