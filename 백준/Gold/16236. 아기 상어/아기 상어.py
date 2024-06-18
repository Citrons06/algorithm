from collections import deque

def shark(n, space):
    global start_shark
    shark_size = 2
    total_dist = 0
    eat = 0

    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                start_shark = (i, j)
                space[i][j] = 0

    while True:
        eat_fish = BFS(n, start_shark, shark_size, space)
        if not eat_fish:
            break

        eat += 1
        dist, x, y = eat_fish[0]
        total_dist += dist

        start_shark = (x, y)
        space[x][y] = 0

        if eat == shark_size:
            shark_size += 1
            eat = 0

    return total_dist

# 가까운 먹이 탐색
def BFS(n, start, size, space):

    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])  #초기 상어 위치

    visited = [[False] * n for _ in range(n)]
    visited[start[0]][start[1]] = True

    dist = [[0] * n for _ in range(n)]

    eat_fish = []
    while queue:
        x, y = queue.popleft()

        for dx, dy in dir:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if space[nx][ny] <= size:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

                    dist[nx][ny] = dist[x][y] + 1
                    if 0 < space[nx][ny] < size:
                        eat_fish.append((dist[nx][ny], nx, ny))

    eat_fish.sort()
    return eat_fish

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
print(shark(n, space))