n = int(input())
X = list(map(int, input().split()))

# Xi` 값은 현재 리스트(X)에서 본인보다 작은 원소의 개수
# ! 중복 제거 / 딕셔너리에 인덱스와 원소 값 저장
sort_X = sorted(set(X))
idx_dict = {}
for idx, val in enumerate(sort_X):
    idx_dict[val] = idx  # 원소 값으로 인덱스를 찾기 위해 {val: idx} 형태로 저장

for x_ins in X:
    print(idx_dict.get(x_ins), end=' ')
