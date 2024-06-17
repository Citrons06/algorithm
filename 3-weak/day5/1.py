# 리스트의 최솟값부터 탐색
# 최솟값을 1씩 증가시키면서 나누어 떨어지는 수 탐색, 3개 이상 찾으면 break

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