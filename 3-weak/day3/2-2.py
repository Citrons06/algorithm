n = int(input())
peaks = list(map(int, input().split()))

stack = []
kill = [0] * n

for i in range(n):
    # 현재 피크보다 낮은 피크 제거, 제거된 피크에 대한 kill 값 갱신
    while stack and peaks[stack[-1]] < peaks[i]:
        kill[stack.pop()] = i - stack[-1] - 1

    stack.append(i)

# 스택에 남아 있는 피크 비교
while stack:
    if stack:
        kill[stack.pop()] = n - stack[-1] - 1
    else:
        kill[stack.pop()] = n - 1

print(max(kill))