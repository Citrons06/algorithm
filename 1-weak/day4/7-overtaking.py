from collections import deque

n = int(input())
in_car = deque()
out_car = deque()

over_cnt = 0

for i in range(n):
    in_car.append(input())

for i in range(n):
    out_car.append(input())

while len(out_car):

    # 두 리스트의 첫 번째 차량이 같으면 덱에서 꺼내기만 함
    if in_car[0] == out_car[0]:
        in_car.popleft()
        out_car.popleft()

    # 같지 않다면 over cnt ++
    else:
        over_cnt += 1
        in_car.remove(out_car.popleft())

print(over_cnt)