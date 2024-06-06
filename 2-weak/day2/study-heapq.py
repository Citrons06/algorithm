import heapq
from heapq import *

a = [5, 3, 4, 1, 2]
heapify(a)  # a를 최소힙으로 변환
print(a[0])  # 1
print(heappop(a))  # 최솟값 추출
print(a[0])  # 1 제거 -> 남아 있는 최솟값 2 반환
heappush(a, 7)  # a라는 힙에 7 추가
print(a[0])  # 2
heappush(a, 0)  # a라는 힙에 0 추가
print(a[0])  # 0

### 최소 힙 ###
# heapq 모듈은 기본적으로 최소 힙을 제공한다.
# 최대 힙을 구현하려면, 삽입할 때 값의 부호를 바꾸는 방법을 사용한다.

# 최소 힙 생성 및 삽입
min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 2)

# 최솟값 확인 (최소 힙에서는 루트가 최솟값)
min_value = min_heap[0]
print('최솟값 (Min Heap):', min_value)

# 최대 힙 생성 (음수 값을 이용)
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)

# 최댓값 확인 (최대 힙에서는 루트의 음수 값이 최댓값)
max_value = max_heap[0]
print('최댓값 (Max Heap):', max_value)