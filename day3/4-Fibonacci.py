n = int(input())

def recur(n):
    f = [0] * (n + 1)
    f[1] = f[2] = 1

    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]

print(recur(n), n - 2)

# 31120KB 40ms