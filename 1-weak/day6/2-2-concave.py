def check_five_in_a_row(concave, stone):
    # 가로 체크
    for i in range(19):
        for j in range(15):
            if all(concave[i][j + k] == stone for k in range(5)):
                if (j == 0 or concave[i][j - 1] != stone) and (j + 5 == 19 or concave[i][j + 5] != stone):
                    return (stone, i + 1, j + 1)

    # 세로 체크
    for i in range(19):
        for j in range(15):
            if all(concave[j + k][i] == stone for k in range(5)):
                if (j == 0 or concave[j - 1][i] != stone) and (j + 5 == 19 or concave[j + 5][i] != stone):
                    return (stone, j + 1, i + 1)

    # 대각선 체크 (왼위 -> 오아)
    for i in range(15):
        for j in range(15):
            if all(concave[i + k][j + k] == stone for k in range(5)):
                if (i == 0 or j == 0 or concave[i - 1][j - 1] != stone) and (
                        i + 5 == 19 or j + 5 == 19 or concave[i + 5][j + 5] != stone):
                    return (stone, i + 1, j + 1)

    # 대각선 체크 (오위 -> 왼아)
    for i in range(15):
        for j in range(4, 19):
            if all(concave[i + k][j - k] == stone for k in range(5)):
                if (i == 0 or j == 18 or concave[i - 1][j + 1] != stone) and (
                        i + 5 == 19 or j - 5 == -1 or concave[i + 5][j - 5] != stone):
                    return (stone, i + 1, j + 1)

    return (0, 0, 0)


concave = [list(map(int, input().split())) for _ in range(19)]
result = (0, 0, 0)

for stone in [1, 2]:
    result = check_five_in_a_row(concave, stone)
    if result[0] != 0:
        break

print(result[0])
if result[0] != 0:
    print(result[1], result[2])