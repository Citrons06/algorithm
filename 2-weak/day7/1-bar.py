import sys
input = sys.stdin.readline

# n개의 막대에 대한 높이 정보가 주어질 때 오른쪽에서 보이는 막대의 개수
# ! 맨 마지막으로 오는 막대의 높이보다 높은 막대의 개수 세기
n = int(input())
m = [int(input()) for _ in range(n)]

# ! 마지막 막대보다 길다고 해도 뒤의 막대보다 짧으면 보이지 않음 (max 변수 추가)
max_bar = m[-1]
cnt = 1  # 보이는 막대 수

# 오른쪽에서 보이는 막대의 개수 세기(cnt++)
for i in range(n-2, -1, -1):
    # 리스트를 거꾸로 돌면서 더 긴 막대가 있으면 max 값 갱신 / cnt++
    if max_bar < m[i]:
        cnt += 1
        max_bar = m[i]

print(cnt)
