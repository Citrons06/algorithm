from collections import deque

n, l = map(int, input().split())
mydeque = deque()
list = list(map(int, input().split()))

# 새로운 값이 들어올 때마다 현재 수보다 큰 값을 덱에서 제거해 시간 복잡도 줄임
for i in range(n):

    while mydeque and mydeque[-1][0] > list[i]:
        mydeque.pop()
    mydeque.append((list[i], i))

    if mydeque[0][1] <= i - l: # 범위에서 벗어난 값 제거
        mydeque.popleft()
    print(mydeque[0][0], end=' ')
