score = [int(input()) for _ in range(10)]

cur_sum = 0
sum = 0

for s in score:
    cur_sum += s
    if abs(100 - cur_sum) <= abs(100 - sum):
        if cur_sum > sum:
            sum = cur_sum

print(sum)