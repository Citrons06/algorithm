from collections import deque

def cal_truck(t):
    bridge = deque([0] * w)
    cur_weight = 0
    sec = 0
    truck_idx = 0

    while truck_idx < n or cur_weight > 0:
        sec += 1

        cur_weight -= bridge.popleft()

        if truck_idx < n:
            if cur_weight + truck_weight[truck_idx] <= L:
                bridge.append(truck_weight[truck_idx])
                cur_weight += truck_weight[truck_idx]
                truck_idx += 1
            else:
                bridge.append(0)

    return sec

n, w, L = map(int, input().split())
truck_weight = list(map(int, input().split()))

print(cal_truck(truck_weight))