a, b = map(int, input().split())

A = []
for i in range(b + 1):
    for j in range(i):
        A.append(i)

# 합배열
S = [0]
temp = 0
for i in A:
    temp += i
    S.append(temp)

print(S[b] - S[a-1])