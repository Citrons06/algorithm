n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

ans = []

for i in range(len(board) - 7):
    for j in range(m - 7):
        w_cnt, b_cnt = 0, 0

        for row in range(i, i + 8):
            for col in range(j, j + 8):

                if (row + col) % 2 == 0:
                    if board[row][col] == 'B':
                        w_cnt += 1
                    if board[row][col] == 'W':
                        b_cnt += 1

                else:
                    if board[row][col] == 'W':
                        w_cnt += 1
                    if board[row][col] == 'B':
                        b_cnt += 1

        ans.append(w_cnt)
        ans.append(b_cnt)

print(min(ans))