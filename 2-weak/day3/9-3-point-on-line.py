# n: 점의 개수, m: 선분의 개수
n, m = map(int, input().split())
points = sorted(list(map(int, input().split()))) # 좌표: 입력과 동시에 정렬
lines = [list(map(int, input().split())) for _ in range(m)]

for line in lines:
    left, right = line

    # 왼쪽에서 이분 탐색
    while left <= right:
        mid = (left + right) // 2


