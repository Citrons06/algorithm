from collections import deque

def BFS(space, n, m):
    # 이동 방향
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    queue = deque()
    distances = [[-1] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if space[i][j] == 1:
                queue.append((i, j))
                distances[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in dir:
            nx = x + dx
            ny = y + dy

            # 각 칸에 거리 세팅
            if 0 <= nx < n and 0 <= ny < m and distances[nx][ny] == -1:
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))

    max_distance = 0
    for i in range(n):
        for j in range(m):
            if distances[i][j] > max_distance:
                max_distance = distances[i][j]

    return max_distance


n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]

print(BFS(space, n, m))
