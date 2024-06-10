n = int(input())
S = [list(map(int, input().split())) for _ in range(n)]  # 왼쪽 면의 위치, 높이

# 가장 작은 창고 다각형의 면적
# 왼쪽: 최솟값, 중앙: