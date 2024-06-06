import sys
from heapq import *
input = sys.stdin.readline

# push, pop을 할 때 - 부호를 붙여 주기

n = int(input())
heap = []

for _ in range(n):
    a = int(input())

    if a:  # 음수 값 삽입
        heappush(heap, -a)
    else: # a가 0이면 heap에서 최솟값 원소를 뽑고 이를 출력
        if heap:
            print(-heappop(heap))  # 음수 값을 설정했으니 추출할 때 다시 - 붙여 줌
        else:  # heap에 원소가 없으면 0 출력
            print(0)