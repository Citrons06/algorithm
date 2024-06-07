def find_left(points, left, right, target):
    result = right + 1

    while left <= right:
        mid = (left + right) // 2

        if points[mid] >= target:
            result = mid
            right = mid - 1

        else:
            left = mid + 1

    return result

def find_right(points, left, right, target):
    result = left + 1

    while left <= right:
        mid = (left + right) // 2

        if points[mid] >= target:
            result = mid
            left = mid - 1

        else:
            right = mid + 1

    return result

# n: 점의 개수, m: 선분의 개수
n, m = map(int, input().split())
points = sorted(list(map(int, input().split()))) # 좌표: 입력과 동시에 정렬
lines = [list(map(int, input().split())) for _ in range(m)]

for line in lines:
    left, right = line
    idx_left = find_left(points, 0, n-1, left)
    idx_right = find_right(points, 0, n-1, right)

    print(idx_right - idx_left + 1 if idx_left <= idx_right else print(0))