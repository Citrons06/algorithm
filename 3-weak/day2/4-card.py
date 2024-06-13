from itertools import permutations

# 모든 가능한 순서를 고려해야 하므로 permutations 사용

n = int(input())
k = int(input())
num = [input() for _ in range(n)]

combined = set()
for comb in permutations(num, k):
    combined.add(''.join(comb))

print(len(combined))