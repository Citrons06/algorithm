def cal(length, price):
    if min(price) == price[0]:
        return sum(length) * price[0]

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