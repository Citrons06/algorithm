n = int(input())
X = list(map(int, input().split()))

sort_X = sorted(set(X))
idx_dict = {}
for idx, val in enumerate(sort_X):
    idx_dict[val] = idx

for x_ins in X:
    print(idx_dict.get(x_ins), end=' ')
