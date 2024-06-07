n, m = map(int, input().split())
h_wood = list(map(int, input().split()))

left = 0
right = max(h_wood)
result = 0

while left <= right:
    mid = (left + right) // 2
    total = sum(h - mid for h in h_wood if h > mid)

    if total >= m:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
