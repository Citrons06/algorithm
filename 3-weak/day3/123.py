milkcount = int(input())
storemilk = list(map(int, input().split()))

#0, 1, 2
order = [0, 1, 2]
cnt = 0
for i in range(len(storemilk)):
    if storemilk[i] - order[cnt%3] == 0:
        cnt+= 1

print(cnt)