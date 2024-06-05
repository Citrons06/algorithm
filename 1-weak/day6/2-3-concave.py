# 오목 두기

concave = [list(map(int, input().split())) for _ in range(19)]
black = [1, 1, 1, 1, 1]
white = [2, 2, 2, 2, 2]
ans = 0  # 검은색이 이기면 1 / 흰색이 이기면 2 / 승부가 안 나면 0
leng = 0  # 가로
high = 0  # 세로


def width():
    global ans, leng, high
    # 가로로 연달아 5개
    for i in range(19):
        for j in range(15):
            if (concave[i][j:j + 5] == black and (j == 0 or concave[i][j - 1] != 1)
                    and (j + 5 == 19 or concave[i][j + 5] != 1)):  # 다음 오목알이 같은 색일 경우 처리
                ans = 1
                leng = i + 1
                high = j + 1
                return ans

            if (concave[i][j:j + 5] == white and (j == 0 or concave[i][j - 1] != 2)
                    and (j + 5 == 19 or concave[i][j + 5] != 2)):
                ans = 2
                leng = i + 1
                high = j + 1
                return ans

def height():
    global ans, leng, high
    # 세로로 연달아 5개
    for i in range(19):
        for j in range(15):
            if (concave[j:j + 5][i] == black and (j == 0 or concave[j - 1][i] != 1)
                    and (j + 5 == 19 or concave[j + 5][i] != 1)):
                ans = 1
                leng = j + 1
                high = i + 1
                return ans

            if (concave[j:j + 5][i] == black and (j == 0 or concave[j - 1][i] != 1)
                    and (j + 5 == 19 or concave[j + 5][i] != 2)):
                ans = 2
                leng = j + 1
                high = i + 1
                return ans


def cross_top_left():
    global ans, leng, high
    # 대각선으로 연달아 5개(왼위 -> 오아)
    for i in range(15):
        for j in range(15):
            if (all(concave[i + k][j + k] == 1 for k in range(5)) and (
                    i == 0 or j == 0 or concave[i - 1][j - 1] != 1)
                    and (i + 5 == 19 or j + 5 == 19 or concave[i + 5][j + 5] != 1)):
                ans = 1
                leng = i + 1
                high = j + 1
                return ans
            if (all(concave[i + k][j + k] == 2 for k in range(5)) and (
                    i == 0 or j == 0 or concave[i - 1][j - 1] != 2)
                    and (i + 5 == 19 or j + 5 == 19 or concave[i + 5][j + 5] != 2)):
                ans = 2
                leng = i + 1
                high = j + 1
                return ans


def cross_top_right():
    global ans, leng, high
    # 대각선으로 연달아 5개(왼아 -> 오위)
    for i in range(15):
        for j in range(4, 19):
            if (all(concave[i + k][j - k] == 1 for k in range(5)) and (i == 0 or j == 18 or concave[i - 1][j + 1] != 1)
                    and (i + 5 == 19 or j - 5 == -1 or concave[i + 5][j - 4] != 1)):
                ans = 1
                leng = i + 1
                high = j + 1
                return ans
            if (all(concave[i + k][j - k] == 2 for k in range(5)) and (i == 0 or j == 18 or concave[i - 1][j + 1] != 2)
                    and (i + 5 == 19 or j - 5 == -1 or concave[i + 5][j - 4] != 2)):
                ans = 2
                leng = i + 1
                high = j + 1
                return ans

width() or height() or cross_top_left() or cross_top_right()

print(ans)
if ans != 0:
    print(leng, high)
