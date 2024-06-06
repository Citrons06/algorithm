from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
visited = defaultdict(int)
for a in A:
    visited[a] = 1

m = int(input())
targets = list(map(int, input().split()))
for target in targets:
    # 딕셔너리의 get() 함수를 사용하여 target이라는 Key가 없을 때 0으로 설정되도록 함
    print(visited[target])