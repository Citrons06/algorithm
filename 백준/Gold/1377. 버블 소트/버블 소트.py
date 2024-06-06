import sys
input = sys.stdin.readline

n = int(input())
A = []

for i in range(n):
    A.append((int(input()), i))
sorted_A = sorted(A)

max = 0
for i in range(n):
    if max < sorted_A[i][1] - i:
        max = sorted_A[i][1] - i

print(max + 1)