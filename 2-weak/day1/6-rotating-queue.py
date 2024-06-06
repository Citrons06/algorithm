from collections import deque

n, m = map(int, input().split())  # n: 큐의 크기, m: 뽑으려고 하는 수의 개수
loc = list(map(int, input().split()))   # 뽑으려고 하는 수의 위치
que = deque([i for i in range(1, n+1)])

# ! 뽑으려고 하는 원소가 리스트의 첫 번째 위치로 올 때까지 왼or오로 이동
# ! len(que) // 2 보다 작으면 왼쪽, 크면 오른쪽으로 이동 (최솟값)
# ! 이동할 때마다 cnt ++
cnt = 0
for target in loc:
    while True:
        # 첫 번째 원소가 타겟 숫자면 뽑기
        if que[0] == target:
            que.popleft()
            break
        else:
            # 뽑으려는 숫자가 앞쪽에 있을 경우
            if que.index(target) <= len(que) // 2:
                que.rotate(-1)  # 왼쪽으로 한 칸 이동
                cnt += 1
            # 뽑으려는 숫자가 뒷쪽에 있을 경우
            if que.index(target) >= len(que) // 2:
                que.rotate(1)   # 오른쪽으로 한 칸 이동
                cnt += 1

print(cnt)