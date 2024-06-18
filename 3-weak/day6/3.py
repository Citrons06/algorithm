import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def cal_distance(x1, y1, x2, y2):
    dist = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5
    return dist

def dijkstra():
    dists = [float('inf') for _ in range(n + 2)]
    dists[0] = 0.0
    q = []
    heappush(q, [0.0, 0])

    while q:
        cur_cost, cur_node = heappop(q)

        if dists[cur_node] < cur_cost:
            continue

        if cur_node == n + 1:
            continue

        for next_node, next_cost in nodes[cur_node]:
            if dists[next_node] > next_cost + cur_cost:
                dists[next_node] = next_cost + cur_cost
                heappush(q, [next_cost + cur_cost, next_node])

    return dists[n + 1]

# 입력 받기
start_x, start_y = map(float, input().split())
goal_x, goal_y = map(float, input().split())
n = int(input())

pos = []
for i in range(1, n+1):
    cur_x, cur_y = map(float, input().split())
    pos.append([cur_x, cur_y])
pos.insert(0, [start_x, start_y])
pos.append([goal_x, goal_y])

nodes = [[] for _ in range(n+1)]

for idx in range(1, n + 2):
    x2, y2 = pos[idx]
    dist = cal_distance(pos[0][0], pos[0][1], x2, y2)
    nodes[0].append([idx, dist / 5.0])

for idx in range(1, n + 1):
    x1, y1 = pos[idx]
    dist = cal_distance(x1, y1, pos[n + 1][0], pos[n + 1][1])
    nodes[idx].append([n + 1, dist / 5.0])
    nodes[idx].append([n + 1, 2.0 + (abs(dist - 50.0 / 5.0))])

for i in range(1, n+1):
    x1, y1 = pos[i]
    for j in range(i+1, n+1):
        x2, y2 = pos[j]
        distance = cal_distance(x1, y1, x2, y2)
        nodes[i].append([j, distance/5.0])
        nodes[i].append([j, 2.0 + (abs(distance-50.0) / 5.0)])
        nodes[j].append([i, distance/5.0])
        nodes[j].append([i, 2.0 + (abs(distance-50.0) / 5.0)])

print(dijkstra())