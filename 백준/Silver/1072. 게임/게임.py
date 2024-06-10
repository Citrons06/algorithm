import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = (y * 100) // x

def win_per(x, y):
    return (y * 100) // x

if x == y or z >= 99:
    print(-1)

else:
    cnt = 0
    left = 0
    right = x

    while left <= right:
        mid = (left + right) // 2

        if win_per(x + mid, y + mid) != z:
            cnt = mid
            right = mid - 1
        else:
            left = mid + 1

    print(cnt)