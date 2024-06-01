n = int(input())
m = int(input())
s = input()

# 투포인터
left_idx = 0
right_idx = 0
cnt = 0

while right_idx < m:
    if s[right_idx: right_idx + 3] == 'IOI':
        right_idx += 2
        if right_idx - left_idx == 2 * n:
            cnt += 1
            left_idx += 2

    else:
        left_idx = right_idx = right_idx + 1

print(cnt)