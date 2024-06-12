import math

# (지각 시간)**2 = 일찍 마쳐 주는 시간
# 수업 시간 > 일찍 마쳐 주는 시간 + (지각 시간)**2

t = int(input())
class_times = [int(input()) for _ in range(t)]

for class_time in class_times:
    # 최대 지각 시간을 수업 시간의 제곱근으로 세팅 후
    max_tardy_time = int(math.sqrt(class_time))

    # 수업 시간을 초과하지 않는 최댓값을 찾음
    while max_tardy_time + max_tardy_time ** 2 > class_time:
        max_tardy_time -= 1

    print(max_tardy_time)
