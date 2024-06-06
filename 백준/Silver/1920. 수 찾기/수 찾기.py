import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

check = {}
for a in A:
    check[a] = 1

m = int(input())
m_num = list(map(int, input().split()))

for num in m_num:
    print(check.get(num, 0))
