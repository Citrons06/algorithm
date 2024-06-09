x, y = map(int, input().split())  # 게임 횟수, 이긴 게임
# x, y의 값이 얼마나 올라가야 '(y // x) * 100'의 값이 변하는가?
z = (y // x) * 100

cnt = 0
left = 0
right = 10 ** 9

def win_per(x, y):
    return (y // x) * 100

if x == y:
    pass
else:
    while left <= right:
        mid = (left + right) // 2
