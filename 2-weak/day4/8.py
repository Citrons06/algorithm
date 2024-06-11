def cal_bar(n, S):
    S.sort()

    max_h = 0
    max_idx = 0
    for i in range(n):
        if S[i][1] > max_h:
            max_h = S[i][1]
            max_idx = i

    # 왼 -> max 기둥 면적 계산
    area = 0
    pre_high = S[0][1]
    for i in range(1, max_idx + 1):
        # 현재 기둥이 이전 기둥보다 높으면 높이 업데이트
        if S[i][1] > pre_high:
            area += (S[i][0] - S[i-1][0]) * pre_high
            pre_high = S[i][1]
        else:
            area += (S[i][0] - S[i-1][0]) * pre_high

    area += max_h  # + max 기둥 면적

    # 오 -> max 기둥 면적 계산
    pre_high = S[-1][1]
    for i in range(n - 2, max_idx - 1, -1):
        if S[i][1] > pre_high:
            area += (S[i+1][0] - S[i][0]) * pre_high
            pre_high = S[i][1]
        else:
            area += (S[i+1][0] - S[i][0]) * pre_high

    return area

# 가장 작은 창고 다각형의 면적
# 왼쪽: 최솟값에서 점점 늘어남, 오른쪽: 최댓값에서 점점 줄어듦 이런 흐름,,
# 즉 면적의 최솟값은 왼 -> max 기둥 면적 + 오 -> max 기둥 면적

# 입력
n = int(input())
S = [list(map(int, input().split())) for _ in range(n)]  # 왼쪽 면의 위치, 높이

print(cal_bar(n, S))