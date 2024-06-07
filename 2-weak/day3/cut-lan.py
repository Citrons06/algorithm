n, k = map(int, input().split())  # 전체 랜선의 갯수, 만들어야 하는 갯수
lines = [int(input()) for _ in range(n)]  # 가지고 있는 랜선의 길이 리스트
ans = 1
left = 1
right = 2 ** 31 - 1  # 문제에서 가능한 랜선 길이의 최대치를 설정하기 위한 임의의 큰 값
while left <= right:
    mid = (left + right) // 2  # 중간 값만큼 랜선을 자름
    cnt = 0  # 현재 mid 길이로 잘랐을 때 만들 수 있는 랜선의 총 개수
    for line in lines:
        cnt += line // mid  # 전선 길이로 나눈 몫이 만들 수 있는 전선의 개수
        print(cnt)

    # 현재 길이(mid)로 잘랐을 때 요구하는 랜선 개수(k) 이상을 만들 수 있다면 정답 갱신
    if cnt >= k:
        ans = mid       # 현재 길이를 최대 랜선 길이로 갱신
        left = mid + 1  # 정답을 최대로 늘려야 하기 때문에 탐색 범위를 큰 쪽으로 옮겨 줌
    else:
        right = mid - 1

print(ans)

