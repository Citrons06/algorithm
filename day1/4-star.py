n = int(input())

# i * '*' + ' ' * (2 * (n - i)) + n * '*'
for i in range(1, n+1):
    print(i * '*' + ' ' * 2 * (n - i) + i * '*')

for j in range(n - 1, 0, -1):
    print(j * '*' + ' ' * 2 * (n - j) + j * '*')