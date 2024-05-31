n = int(input())
m = int(input())
a = list(map(int, input().split()))

a.sort()

start_idx = 0
end_idx = n - 1
cnt = 0

while start_idx < end_idx:
    if a[start_idx] + a[end_idx] < m:
        start_idx += 1
    elif a[start_idx] + a[end_idx] > m:
        end_idx -= 1
    else:
        cnt += 1
        start_idx += 1
        end_idx -= 1

print(cnt)