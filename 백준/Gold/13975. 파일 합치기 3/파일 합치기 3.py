import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    chapter = int(input())
    files = list(map(int, input().split()))

    heapq.heapify(files)
    ans = 0
    while len(files) > 1:
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        sum = 0
        sum += a + b
        ans += sum

        heapq.heappush(files, sum)

    print(ans)