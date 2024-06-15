def find_combi_per(n):
    while len(n) > 2:
        new_combi = ''

        for i in range(1, len(n)):
            sum_combi = int(n[i-1]) + int(n[i])
            new_combi += str(sum_combi % 10)  # 한 자리 숫자로 변환

        n = new_combi
    return n

A = str(input())
B = str(input())

combi = ''
for i in range(8):
    combi += A[i]
    combi += B[i]

print(find_combi_per(combi))