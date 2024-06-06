n = int(input())
A = list(map(int, input().split())) # [4, 1, 5, 2, 3]
visited = {}
for a in A:
    visited[a] = 1  # {4: 1, 1: 1, 5: 1, 2: 1, 3: 1}

m = int(input())
targets = list(map(int, input().split())) # [1, 3, 7, 9, 5]
for target in targets:
    # 딕셔너리의 get() 함수를 사용하여 target이라는 Key가 없을 때 0으로 설정되도록 함
    print(visited.get(target, 0))