import sys

input = sys.stdin.readline

def max_meeting(time):
    time.sort(key=lambda x: (x[1], x[0]))

    end_point = 0
    cnt = 0

    for start, end in time:
        if end_point <= start:
            cnt += 1
            end_point = end

    return cnt

n = int(input())

time = []
for _ in range(n):
    start_end = tuple(map(int, input().split()))
    time.append(start_end)

print(max_meeting(time))