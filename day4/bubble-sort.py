n = int(input())
A = []

for i in range(n):
    A.append(int(input()))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if A[j] > A[j + 1]:
            temp = A[j]
            A[j] = A[j + 1]
            A[j + 1] = temp

for i in range(n):
    print(A[i])