n = int(input())
a = list(map(int, input().split()))
a.sort()
cnt = 0

for k in range(n):

    find = a[k]
    i = 0
    j = n - 1

    while i < j:
        if find == a[i] + a[j]:
            if i != k and j != k:
                cnt += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1

        elif find > a[i] + a[j]:
            i += 1
        else:
            j -= 1

print(cnt)