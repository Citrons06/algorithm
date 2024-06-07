n, m = map(int, input().split())
h_wood = list(map(int, input().split()))  # 나무의 높이 리스트

left = 0
right = max(h_wood)
ans = 0  # 절단기 높이의 최댓값

# ! 나무의 높이가 mid보다 높으면 mid를 기준으로 모든 나무 절단
# ! 절단한 나무의 합과 원하는 길이를 비교하며 탐색 범위 조절
while left <= right:
    mid = (left + right) // 2
    total = sum(h - mid for h in h_wood if h > mid)  # 잘린 나무의 총 길이

    # 원하는 길이보다 길면 절단기 높이 높임
    if total >= m:
        ans = mid
        left = mid + 1
    # 원하는 길이보다 짧으면 절단기 높이 낮춤
    else:
        right = mid - 1

print(ans)