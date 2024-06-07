import bisect

n, m = map(int, input().split())
points = list(map(int, input().split()))
lines = [tuple(map(int, input().split())) for _ in range(m)]

points.sort()

for left, right in lines:
    left_index = bisect.bisect_left(points, left)
    right_index = bisect.bisect_right(points, right) - 1
    
    if left_index <= right_index:
        count = right_index - left_index + 1
    else:
        count = 0
    
    print(count)