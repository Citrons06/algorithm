### 시간 초과 ###
n = int(input())
X = list(map(int, input().split()))

# Xi` 값은 현재 리스트(X)에서 본인보다 작은 원소의 개수
# ! 중복 제거 후 정렬한 리스트에서 본인의 인덱스 값 탐색
sort_X = sorted(set(X))

for x_ins in X:
    print(sort_X.index(x_ins), end=' ')

# 시간 초과 사유
# N의 최대 범위가 1,000,000 이고 sort_X.index(x_ins) 부분에서 O(n^2) 걸린 것 같음,,