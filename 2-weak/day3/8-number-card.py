n = int(input())  # 숫자 카드의 개수
card_num = list(map(int, input().split()))  # 숫자 카드에 적혀 있는 수
m = int(input())
find_num = list(map(int, input().split()))  # 가지고 있는 숫자인지 판별될 수

# ! 해시
check = {}
for num in card_num:
    check[num] = 1

for num in find_num:
    print(check.get(num, 0), end=' ')