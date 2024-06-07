n = int(input())
atm_time = list(map(int, input().split()))

sort_time = sorted(atm_time)

sum_time = [0] * n
sum_time[0] = sort_time[0]
for i in range(1, n):
    sum_time[i] = sum_time[i-1] + sort_time[i]

print(sum(sum_time))