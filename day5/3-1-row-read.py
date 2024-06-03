A = [list(map(str, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(len(A[i])):
        for z in range(len(A[i][j])):
            print(A[z][j][i], end='')
### IndexError ###