import bisect

# 입력 받기
n, m = map(int, input().split())
points = list(map(int, input().split()))
lines = [tuple(map(int, input().split())) for _ in range(m)]

# 점들을 정렬
points.sort()

# 각 선분에 대해 포함된 점의 개수를 계산
for left, right in lines:
    # left 이상인 첫 번째 점의 인덱스 찾기
    left_index = bisect.bisect_left(points, left)
    # right 이하인 마지막 점의 인덱스 찾기
    right_index = bisect.bisect_right(points, right) - 1

    # 포함된 점의 개수 계산
    if left_index <= right_index:
        count = right_index - left_index + 1
    else:
        count = 0

    # 결과 출력
    print(count)