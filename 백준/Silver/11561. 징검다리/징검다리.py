t = int(input())

for _ in range(t):
    stone = int(input())

    start = 0
    end = stone
    cnt = 0
    while start <= end:
        mid = (start + end) // 2
        sum = mid * (mid + 1) // 2

        if sum <= stone:
            cnt = max(mid, cnt)
            start = mid + 1
        else:
            end = mid - 1

    print(cnt)