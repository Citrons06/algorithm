n = int(input())  # 스위치 개수
sts = list(map(int, input().split()))  # 스위치 상태
stu = int(input())  # 학생 수
A = [list(map(int, input().split())) for _ in range(stu)]  # 성별, 부여 번호

for i in range(stu):

    if A[i][0] == 1:  # 남자

        for j in range(1, n + 1):
            if j % A[i][1] == 0:
                sts[j - 1] = 1 - sts[j - 1]

    if A[i][0] == 2:  # 여자
        idx = A[i][1] - 1  # 시작인덱스
        sts[idx] = 1 - sts[idx]

        for j in range(1, n // 2 + 1):
            if idx - j >= 0 and idx + j < n and sts[idx + j] == sts[idx - j]:
                sts[idx - j] = 1 - sts[idx - j]
                sts[idx + j] = 1 - sts[idx + j]
            else:
                break

for i in range(0, n, 20):
    print(' '.join(map(str, sts[i : i + 20])))