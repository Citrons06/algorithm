import sys
input = sys.stdin.readline

x, y = map(int, input().split())  # 게임 횟수, 이긴 게임
# x, y의 값이 얼마나 올라가야 '(y // x) * 100'의 값이 변하는가?
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