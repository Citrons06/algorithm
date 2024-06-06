n = int(input())
fruit_count = {}

for _ in range(n):
    fruit, count = input().split()
    count = int(count)

    if fruit in fruit_count:
        fruit_count[fruit] += count
    else:
        fruit_count[fruit] = count

print('YES' if 5 in fruit_count.values() else 'NO')