import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input().strip())
heap = []

for _ in range(n):
    a = int(input().strip())


    if a != 0:   # a가 0이 아니면 heap에 삽입
        # (절댓값, 원래의 값) 튜플 형태로 heap에 추가
        # abs(a): 우선순위 큐에서 절댓값 기준으로 정렬하기 위한 키
        # 이제 heap은 항상 절댓값이 작은 순서대로 정렬된다.
        heappush(heap, (abs(a), a))
    else:
        # 입력값이 0이면 힙에서 절댓값이 가장 작은 값을 뽑아서 출력
        # 절댓값이 같은 경우 원래의 값이 작은 순서대로 출력
        if heap:
            print(heappop(heap)[1]) # 저장된 요소가 튜플 -> 튜플의 1번 인덱스인 a 반환
        else:
            print(0)