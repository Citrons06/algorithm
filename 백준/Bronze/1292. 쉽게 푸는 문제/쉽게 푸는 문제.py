a, b = map(int, input().split())

A = []
for i in range(1, b+1):
    A.extend([i] * i)

sum_A = [0] * len(A)
sum_A[0] = A[0]
for i in range(1, len(A)):
    sum_A[i] = sum_A[i-1] + A[i]

if a > 1:
    print(sum_A[b-1] - sum_A[a-2])
else:
    print(sum_A[b-1])
