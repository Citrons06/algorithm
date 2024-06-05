n, m, r = map(int, input().split()) # n, m: 배열의 크기 / r: 회전 수
A = [list(map(int, input().split())) for _ in range(n)]

def rotate():
    for layer in range(min(n, m) // 2):
        temp = []

        for i in range(layer, m - layer - 1):
            temp.append(A[layer][i])

        for i in range(layer, n - layer - 1):
            temp.append(A[i][m - layer - 1])

        for i in range(m - layer - 1, layer, -1):
            temp.append(A[n - layer - 1][i])

        for i in range(n - layer - 1, layer, -1):
            temp.append(A[i][layer])

        rotation = r % len(temp)
        temp = temp[rotation:] + temp[:rotation]

        idx = 0
        for i in range(layer, m - layer - 1):
            A[layer][i] = temp[idx]
            idx += 1

        for i in range(layer, n - layer - 1):
            A[i][m - layer - 1] = temp[idx]
            idx += 1

        for i in range(m - layer - 1, layer, -1):
            A[n - layer - 1][i] = temp[idx]
            idx += 1

        for i in range(n - layer - 1, layer, -1):
            A[i][layer] = temp[idx]
            idx += 1

for _ in range(r):
    rotate()

for row in A:
    print(' '.join(map(str, row)))
