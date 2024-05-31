from queue import PriorityQueue

import sys
print = sys.stdout.write
input = sys.stdin.readline

n = int(input())
myQueue = PriorityQueue()

for i in range(n):
    request = int(input())

    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str((temp[1])) + '\n')

    else:
        # 절댓값을 기준으로 정렬
        # 값이 같으면 음수 우선 정렬
        myQueue.put((abs(request), request))