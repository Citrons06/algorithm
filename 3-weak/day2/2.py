### 시간 초과..
from itertools import permutations

# 부분 합
def part_sum(start, end, A):
    return sum(A[start:end + 1])

# 청정수열 점수 계산
def cal_score(perm, n):
    score = 0
    for i in range(1, n + 1):
        idx = [j for j, x in enumerate(perm) if x == i]
        score += part_sum(idx[0], idx[1], perm)

    return score

# 청정수열: 길이가 2n 이고 1부터 n까지의 정수들이 두 번씩 등장하는 수열
# 길이가 2n 이면서 점수가 최소인 청정수열의 수

# 모든 순열을 생성해서 청정수열 점수를 계산하고, 점수의 최솟값 갯수 계산
n = int(input())

A = []
for i in range(1, n + 1):
    A.append(i)
    A.append(i)

scores = []

# 모든 순열 생성 후 청정수열 점수 계산
for perm in set(permutations(A)):
    score = cal_score(perm, n)
    scores.append(score)

# 청정 수열 점수의 최솟값을 가진 수열의 수 세기
print(scores.count(min(scores)))