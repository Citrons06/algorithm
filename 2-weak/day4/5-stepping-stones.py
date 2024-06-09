t = int(input())

# ! 징검다리를 가장 많이 밟고 가는 경우는 1->2->4->7 처럼 건너는 거리를 1씩 늘리는 경우
# ! 등차수열의 합 공식 이용
for _ in range(t):
    stone = int(input())

    start = 0
    end = stone
    cnt = 0  # 건널 수 있는 징검다리 개수의 최댓값
    while start <= end:
        mid = (start + end) // 2  # 현재 시도하는 징검다리의 개수
        sum = mid * (1 + mid) // 2  # mid 개의 징검다리를 밟을 때 돌 개수

        if sum <= stone:
            cnt = max(mid, cnt)  # mid가 기존 징검다리 개수보다 작으면 cnt 값에 업데이트
            start = mid + 1

        # mid 값이 stone 보다 크면 유효한 경우가 아님 -> 범위 줄임
        else:
            end = mid - 1

    print(cnt)