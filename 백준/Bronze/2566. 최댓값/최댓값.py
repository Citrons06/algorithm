A = [list(map(int, input().split())) for _ in range(9)]
max_val = -1
row_idx = 0 # 가로
col_idx = 0 # 세로

for i in range(9):
    for j in range(9):
        if max_val < A[i][j]:
            max_val = A[i][j]
            row_idx = i + 1
            col_idx = j + 1

print(max_val)
print(row_idx, col_idx)