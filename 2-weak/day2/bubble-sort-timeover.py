import sys
input = sys.stdin.readline

n = int(input())
A = [int(input().rstrip()) for _ in range(n)]

changed = False
def bubble_sort():
    global changed
    for i in range(1, n+1):
        changed = False

        for j in range(n-i):
            if A[j] > A[j+1]:
                changed = True
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp

        # 버블 정렬이 한 번도 일어나지 않은 루프 위치
        if changed == False:
            print(i)
            break

bubble_sort()