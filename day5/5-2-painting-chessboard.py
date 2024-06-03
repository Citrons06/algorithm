n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

ans = []

# 8*8 체스판을 오른쪽, 아래로 한 칸 씩 움직이면서 cnt 비교
# 완성된 체스판의 경우의 수는 [W로 시작하는 경우, B로 시작하는 경우] 2가지
for i in range(len(board) - 7):
    for j in range(m - 7):
        w_cnt, b_cnt = 0, 0 # white, black으로 시작할 때 다시 칠해야 하는 개수

        for row in range(i, i + 8):
            for col in range(j, j + 8):

                # 해당 칸이 black일 경우
                if board[row][col] == 'B':
                    # 첫 칸이 white인 경우
                    # 행과 열의 합이 짝수일 때 흰색으로 칠해야 함
                    if (row + col) % 2 == 0:
                        w_cnt += 1
                    # 첫 칸이 black인 경우
                    # 행과 열의 합이 홀수일 때 검정색으로 칠해야 함
                    if (row + col) % 2 != 0:
                        b_cnt += 1

                # 해당 칸이 white일 경우
                if board[row][col] == 'W':
                    if (row + col) % 2 == 0:
                        b_cnt += 1
                    if (row + col) % 2 != 0:
                        w_cnt += 1

        ans.append(w_cnt)
        ans.append(b_cnt)

print(min(ans))