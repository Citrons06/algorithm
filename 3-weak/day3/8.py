from heapq import heappop, heappush

def dijkstra(start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    queue = [(0, start)]

    while queue:
        cost, idx = heappop(queue)
        if dist[idx] < cost:
            continue

        for adj, d in A[idx]:
            if dist[adj] > cost + d:
                dist[adj] = cost + d
                heappush(queue, (dist[adj], adj))

    return dist

INF = float('inf')

n = int(input())
m = int(input())

A = [[] for _ in range(n + 1)]
for _ in range(m):
    start_num, end_num, pay = map(int, input().split())
    A[start_num].append((end_num, pay))

start_city, end_city = map(int, input().split())

# start_city에서의 최단 경로를 계산
dist_from_start = dijkstra(start_city)

min_pay = dist_from_start[end_city]
print(min_pay)