n, m = map(int, input().split())
square = [list(input()) for _ in range(n)]
ans = []

for row in range(n):
    for col in range(m):

        for i in range(min(m, n)):
            # out of index 예외 처리
            # 가로, 세로 길이를 1씩 늘려가며 비교 후 조건에 맞는 정사각형 크기 계산
            if row + i < n and col + i < m and square[row][col] == square[row + i][col] == square[row][col + i] == square[row + i][col + i]:
                cnt = i
                ans.append((cnt+1) ** 2)

print(max(ans))