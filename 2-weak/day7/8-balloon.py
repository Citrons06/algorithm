import sys
from collections import deque

input = sys.stdin.readline

# 터진 풍선 번호의 인덱스+1 출력
# ! 원본 인덱스 번호 복원을 위해 enumerate() 사용

n = int(input())
b = deque(list(enumerate((map(int, input().split())), start=1)))
ans = []  # 정답 리스트

# ! 덱을 모두 비울 때까지 덱을 돌리면서 원본 인덱스를 정답 리스트에 저장
while b:
    idx, num = b.popleft()
    ans.append(idx)

    # 풍선 안의 값이 양수이면 -(num - 1) 만큼 왼쪽으로 돌림
    if num > 0:
        b.rotate(-(num - 1))
    # 풍선 안의 값이 음수이면 -num 만큼 오른쪽으로 돌림
    if num < 0:
        b.rotate(-num)

print(*ans)