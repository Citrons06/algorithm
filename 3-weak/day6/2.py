def find_max(k, n, sensor):
    if k >= n:
        return 0

    dist = []
    for i in range(1, n):
        dist.append(sensor[i] - sensor[i - 1])
    dist.sort()

    for _ in range(k - 1):
        dist.pop()

    return sum(dist)

n = int(input()) # 센서의 개수
k = int(input()) # 집중국의 개수
sensor = list(map(int, input().split()))
sensor.sort()

print(find_max(k, n, sensor))