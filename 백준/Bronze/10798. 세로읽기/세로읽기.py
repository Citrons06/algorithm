A = [input() for _ in range(5)]
max_len = max(len(line) for line in A)

ans = ''

for i in range(max_len):
    for line in A:
        if i < len(line):
            ans += line[i]

print(ans)