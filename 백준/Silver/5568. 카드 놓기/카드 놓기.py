from itertools import permutations

n = int(input())
k = int(input())
num = [input().strip() for _ in range(n)]

combined = set()
for comb in permutations(num, k):
    combined.add(''.join(comb))

print(len(combined))