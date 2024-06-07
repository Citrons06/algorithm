n = int(input())
card_num = list(map(int, input().split()))
m = int(input())
find_num = list(map(int, input().split()))

check = {}
for num in card_num:
    check[num] = 1

for target in find_num:
    print(check.get(target, 0), end=' ')