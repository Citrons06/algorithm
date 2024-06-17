num = list(map(int, input().split()))
min_num = min(num)

while True:
    cnt = 0

    for i in num:
        if min_num % i == 0:
            cnt += 1

    if cnt >= 3:
        break

    min_num += 1

print(min_num)