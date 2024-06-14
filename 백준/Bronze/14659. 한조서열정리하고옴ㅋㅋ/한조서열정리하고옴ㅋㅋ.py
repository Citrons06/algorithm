n = int(input())
peaks = list(map(int, input().split()))

stack = []
kill = [0] * n

for i in range(n):
    while stack and peaks[stack[-1]] < peaks[i]:
        kill[stack.pop()] = i - stack[-1] - 1

    stack.append(i)

while stack:
    if stack:
        kill[stack.pop()] = n - stack[-1] - 1
    else:
        kill[stack.pop()] = n - 1

print(max(kill))