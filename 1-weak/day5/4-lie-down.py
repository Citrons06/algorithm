n = int(input())
A = [list(input()) for _ in range(n)]
row_cnt = 0
col_cnt = 0

# 행에서 자리 찾기
for row in A:
    occ_space = 0  # 차지한 자리

    # .이 연속으로 있을 경우 cnt++
    for i in row:
        if i == '.':
            occ_space += 1
        else:
            if occ_space >= 2:
                row_cnt += 1
            occ_space = 0  # 짐이 있으므로 자리 초기화

    # '.....', '..X..', ... 예외 처리
    if occ_space >= 2:
        row_cnt += 1

# 열에서 자리 찾기
for col in range(n):
    occ_space = 0

    for row in range(n):
        if A[row][col] == '.':
            occ_space += 1
        else:
            if occ_space >= 2:
                col_cnt += 1
            occ_space = 0

    # '.....', '..X..', ... 예외 처리
    if occ_space >= 2:
        col_cnt += 1

print(row_cnt, col_cnt)