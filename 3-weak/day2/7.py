from collections import deque

def cal_truck(t):
    bridge = deque([0] * w)
    cur_weight = 0
    sec = 0
    idx = 0

    while idx < n or cur_weight > 0:
        sec += 1

        # 트럭이 빠져나갈 때마다 현재 하중 감소
        cur_weight -= bridge.popleft()

        if idx < n:
            if cur_weight + t[idx] <= L:
                bridge.append(t[idx])
                cur_weight += t[idx]
                idx += 1
            else:
                bridge.append(0)  # 트럭이 올라갈 수 없으면 빈 공간 유지

    return sec

# n: 트럭 수, w: 다리 길이, L: 최대 하중
n, w, L = map(int, input().split())
truck_weight = list(map(int, input().split()))

print(cal_truck(truck_weight))