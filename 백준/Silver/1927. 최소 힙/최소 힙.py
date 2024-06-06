import sys
from heapq import *
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    a = int(input())
    
    if a:  # a가 0이 아니면 heap에 삽입
        heappush(heap, a)
    else:  # a가 0이면 heap에서 꺼내서 출력
        if heap:
            print(heappop(heap))
        else:  # heap이 비어 있으면 0 출력
            print(0)

