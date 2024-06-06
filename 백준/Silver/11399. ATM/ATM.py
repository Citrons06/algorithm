import sys

input = sys.stdin.readline

def insert_sort(people):
    for i in range(1, len(people)):
        key_point = i
        key = people[i]
        for j in range(i-1, -1, -1):
            if people[j] < people[i]:
                key_point = j + 1
                break
            if j == 0:
                key_point = 0

        for j in range(i, key_point, -1):
            people[j] = people[j-1]
        people[key_point] = key

n = int(input().rstrip())
people = list(map(int, input().split()))
sum_time = [0] * n  # 합배열

insert_sort(people)  # 삽입 정렬

# 합배열 만들기
sum_time[0] = people[0]
for i in range(1, n):
    sum_time[i] = sum_time[i-1] + people[i]

sum = 0
for i in range(n):
    sum += sum_time[i]

print(sum)