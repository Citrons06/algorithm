import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

# A 리스트 원소들을 체크 딕셔너리에 저장 {1: 1, 2: 1}
check = {}
for a in A:
    check[a] = 1

m = int(input())
m_num = list(map(int, input().split()))

# 체크 리스트를 가져올 때 num 값의 Key가 없으면 0 출력
for num in m_num:
    print(check.get(num, 0))