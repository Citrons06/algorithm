def binary_search(arr: list[int], target: int):
    left = 0
    right = len(arr) - 1

    while left <= right:       # left가 right보다 커지면 더 이상 탐색할 범위가 없음
        mid = (left + right) // 2  # 중간 값
        if arr[mid] == target:
            return mid
        if arr[mid] < target:  # 0부터 mid까지 탐색할 필요 없음
            left = mid + 1
        else:                  # mid부터 right까지 탐색할 필요 없음
            right = mid - 1

    return -1 # Not found