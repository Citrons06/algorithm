n = int(input())
m = int(input())
s = str(input())

check_p = 'I' + 'OI' * n

cnt = 0

for i in range(len(s)):

    if s[i : (2 * n) + 1 + i] == check_p:
        cnt += 1

print(cnt)