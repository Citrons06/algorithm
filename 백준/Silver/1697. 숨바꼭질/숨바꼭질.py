from collections import deque


def BFS(v):

    queue = deque([(v, 0)])
    visited[v] = True

    while queue:
        now, sec = queue.popleft()

        if now == bro:
            return sec

        moves = [now - 1, now + 1, now * 2]

        for move in moves:
            if 0 <= move <= 100000 and not visited[move]:
                queue.append((move, sec + 1))
                visited[move] = True

n, bro = map(int, input().split())  # 수빈 위치, 동생 위치
visited = [False] * 100001

print(BFS(n))