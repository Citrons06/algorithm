# d(n)을 직접 구현..?
def d(n):
    str_num = str(n)

    sum = n
    for i in str_num:
        sum += + int(i)

    return sum

d_num = set()  # d(n) 결과 리스트
for i in range(1, 10000):
    d_num.add(d(i))

# 1~10000 수 중 d(n) 결과에 없는 숫자 선별(셀프 넘버 리스트)
self_numbers = [i for i in range(1, 10001) if i not in d_num]

for num in self_numbers:
    print(num)