import sys

input = sys.stdin.readline

n = int(input())
crd = []
for _ in range(n):
    x, y = map(int, input().split())
    crd.append((x, y))

cnt = 0
stack = []

for i in range(n):
    x, y = crd[i]

    if y == 0:
        cnt += len(stack)  # 스택에 남아 있는 빌딩들을 모두 하나의 빌딩으로 처리
        stack = []         # 스택을 비워 주고 다음 빌딩으로 이동
        continue

    while stack and stack[-1] > y:  # 스택이 비어 있지 않고, 스택의 top이 y보다 클 때
        stack.pop()
        cnt += 1

    if not stack or stack[-1] < y:  # 스택이 비어 있거나 스택의 top이 y보다 작을 때
        stack.append(y)

print(cnt + len(stack))  # 스택에 남아 있는 빌딩들을 하나의 빌딩으로 처리