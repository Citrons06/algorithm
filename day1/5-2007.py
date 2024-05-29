m, d = map(int, input().split())

# 1월 1일 = MON
# day % 7 = 0 -> SUN
# ex. 2월 4일(일) -> 31 + 4 = 35, 35 % 7 = 0
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weak = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
sum = 0

# 전월까지의 day 모두 합산
for i in range(m-1):
    sum += day[i]

# sum + 날짜를 7로 나눈 나머지 값을 weak 인덱스에 넣어서 요일 탐색
print(weak[(sum + d) % 7])