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

                # 짝수행의 짝수열 인덱스는 체스판의 첫 색깔과 같음 (색이 번갈아 나오는 체스판의 특성)
                if (row + col) % 2 == 0:
                    if board[row][col] == 'B': # B -> W 로 칠해야 함 (w_cnt++)
                        w_cnt += 1
                    if board[row][col] == 'W': # W -> B 로 칠해야 함 (b_cnt++)
                        b_cnt += 1

                # 체스판의 첫 색깔로 칠해진 나머지 칸의 행+열 값은 홀수임
                else:
                    if board[row][col] == 'W':
                        w_cnt += 1
                    if board[row][col] == 'B':
                        b_cnt += 1

        ans.append(w_cnt)
        ans.append(b_cnt)

print(ans)
print(min(ans))