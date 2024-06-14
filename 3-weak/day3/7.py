import sys

input = sys.stdin.readline

# 회의를 가장 많이 할 수 있는 경우
# 빨리 끝나는 회의 위주로 처리 -> 끝나는 시간 기준으로 오름차순 정렬하고 시작
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