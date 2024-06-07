def search(arr, t):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == t:
            return True
        if arr[mid] < t:
            left = mid + 1
        else:
            right = mid - 1
    return False

n = int(input())
sources = list(map(int, input().split()))
sources.sort()  # 이분 탐색을 하려면 꼭 정렬이 되어 있어야 한다.
m = int(input())
targets = list(map(int, input().split()))
for target in targets:
    print(1 if search(sources, target) else 0)