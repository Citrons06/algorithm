from itertools import combinations

dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))
sorted_dwarfs = sorted(dwarfs)

for comb in combinations(sorted_dwarfs, 7):
    if sum(comb) == 100:
        for i in comb:
            print(i)
        break  # 가능한 조합 아무거나 1개 출력해야 하므로 break
