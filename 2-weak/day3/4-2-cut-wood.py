### 시간 초과 ###
# M 미터의 나무를 얻기 위한 절단기 높이의 최댓값

# n: 나무의 수, m: 가져가려고 하는 나무의 길이
n, m = map(int, input().split())
h_wood = list(map(int, input().split()))  # 나무의 높이 리스트

left = 0
right = max(h_wood)
ans = 0  # 절단기 높이의 최댓값
while left <= right:
    cut = 0  # 잘린 나무의 총 길이
    mid = (left + right) // 2

    for h in h_wood:
        if mid <= h:
            cut += h - mid

    if cut >= m:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)