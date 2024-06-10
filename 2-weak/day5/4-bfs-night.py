import sys
from collections import deque

input = sys.stdin.readline

def BFS(l, start, end):

    # 나이트 이동 방향
    dir = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    # 체스판 칸 수 만큼 방문 리스트 생성
    visited = [[False] * l for _ in range(l)]
    queue = deque([(start[0], start[1], 0)])  # (x, y, 이동 횟수)
    visited[start[0]][start[1]] = True

    while queue:
        x, y, cnt = queue.popleft()

        if (x, y) == end:
            return cnt

        for dx, dy in dir:
            nx = x + dx
            ny = y + dy

            # 좌표 유효성 검사
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt + 1))

# 입력
t = int(input())

ans = []
for _ in range(t):
    l = int(input())  # 체스판 한 변의 길이
    start = tuple(map(int, input().split()))  # 현재 있는 칸
    end = tuple(map(int, input().split()))  # 이동하려고 하는 칸

    ans.append(BFS(l, start, end))

# 출력
for a in ans:
    print(a)