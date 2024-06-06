import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input().strip())
heap = []

for _ in range(n):
    a = int(input().strip())


    if a != 0:

        heappush(heap, (abs(a), a))
    else:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)