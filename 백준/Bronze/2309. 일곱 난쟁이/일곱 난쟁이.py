from itertools import combinations

dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))
sorted_dwarfs = sorted(dwarfs)

for comb in combinations(sorted_dwarfs, 7):
    if sum(comb) == 100:
        for i in comb:
            print(i)
        break
