n, m = map(int, input().split())
square = [list(input()) for _ in range(n)]
ans = []

for row in range(n):
    for col in range(m):

        for i in range(min(m, n)):
            if row + i < n and col + i < m and square[row][col] == square[row + i][col] == square[row][col + i] == square[row + i][col + i]:
                cnt = i
                ans.append((cnt+1) ** 2)

print(max(ans))