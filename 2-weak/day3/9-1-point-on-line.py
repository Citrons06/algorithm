# n: 점의 개수, m: 선분의 개수
n, m = map(int, input().split())
points = list(map(int, input().split())) # 좌표
lines = [list(map(int, input().split())) for _ in range(m)]

for line in lines:
    cnt = 0
    for point in points:
        if line[0] <= point <= line[1]:
            cnt += 1
    print(cnt)