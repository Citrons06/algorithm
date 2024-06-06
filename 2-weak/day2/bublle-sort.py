import sys
input = sys.stdin.readline

n = int(input())
A = []

# 원본 인덱스를 값과 함께 튜플 형식으로 명시적 저장 (원본인덱스, 값)
for i in range(n):
    A.append((int(input()), i))  # [(10, 0), (1, 1), (5, 2), (2, 3), (3, 4)]
sorted_A = sorted(A)  # [(1, 1), (2, 3), (3, 4), (5, 2), (10, 0)]

# 왼쪽으로 가장 많이 이동한 루프(+1)가 swap이 일어나지 않은 곳
# (정렬 전 인덱스) - (정렬 후 인덱스)의 최댓값이 버블 정렬이 완료된 곳
max = 0
for i in range(n):
    if max < sorted_A[i][1] - i:  # 정렬 전 인덱스 - 정렬 후 인덱스 계산의 최댓값 저장
        max = sorted_A[i][1] - i

# 가장 마지막 루프에는 swap이 일어나지 않고 인덱스 값만 증가하므로 +1 처리
print(max + 1)


