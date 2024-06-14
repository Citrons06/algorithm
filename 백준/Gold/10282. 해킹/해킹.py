import sys
from heapq import heappop, heappush

input = sys.stdin.readline

INF = float('inf')

def dijkstra(start, n, A):
    dist = [INF] * (n + 1)
    dist[start] = 0
    queue = [(0, start)]

    while queue:
        cost, idx = heappop(queue)
        if dist[idx] < cost:
            continue

        for adj, s in A[idx]:
            if dist[adj] > cost + s:
                dist[adj] = cost + s
                heappush(queue, (dist[adj], adj))

    return dist

ans = []
for _ in range(int(input())):
    com, d, com_num = map(int, input().split())

    A = [[] for _ in range(com + 1)]
    for _ in range(d):
        a_com, b_com, sec = map(int, input().split())
        A[b_com].append((a_com, sec))

    dist = dijkstra(com_num, com, A)

    hacked_com = sum(1 for x in dist if x < INF)
    max_time = max(x for x in dist if x < INF)

    ans.append(f'{hacked_com} {max_time}')

print('\n'.join(ans))