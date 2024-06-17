def cal(length, price):
    # 첫 도시의 가격이 최솟값이면 그냥 통째로 계산해서 리턴
    if min(price) == price[0]:
        return sum(length) * price[0]

    # for문을 돌면서 현재 최소비용을 발견하면 갱신하면서 계산
    current_min = price[0]
    min_price = 0
    for i in range(len(length)):
        if price[i] <= current_min:
            current_min = price[i]
            min_price += current_min * length[i]
        else:
            min_price += current_min * length[i]

    return min_price

n = int(input())
road_length = list(map(int, input().split()))
L_price = list(map(int, input().split()))

print(cal(road_length, L_price))