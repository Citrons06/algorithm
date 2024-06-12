def d(n):
    str_num = str(n)

    sum = n
    for i in str_num:
        sum += + int(i)

    return sum

d_num = set()
for i in range(1, 10000):
    d_num.add(d(i))

self_numbers = [i for i in range(1, 10001) if i not in d_num]

for num in self_numbers:
    print(num)