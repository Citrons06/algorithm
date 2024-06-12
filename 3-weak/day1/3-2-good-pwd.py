K, L = map(int, input().split())

# L 까지의 수 중 약수가 있는지 확인
for i in range(2, L):
    if K % i == 0:
        print('BAD', i)
        break

else:
    print('GOOD')