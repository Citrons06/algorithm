A = [list(map(int, input().split())) for _ in range(9)]
max_list = [max(A[i]) for i in range(9)]
print(max(max_list))

row_idx = 0 # 가로
col_idx = 0 # 세로

for row in range(9):
    for col in range(9):
        if max(max_list) <= A[row][col]:
            row_idx = row + 1
            col_idx = col + 1

print(row_idx, col_idx)