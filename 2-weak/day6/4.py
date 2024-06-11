import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(graph, node, end, visited, weight_limit):
    if node == end:
        return True

    visited[node] = True

    for neighbor, weight in graph[node]:
        if not visited[neighbor] and weight >= weight_limit:
            if dfs(graph, neighbor, end, visited, weight_limit):
                return True

    return False

# 옮길 수 있는 무게인지 판별
def can_transport_with_weight(graph, start, end, weight):
    visited = [False] * len(graph)
    return dfs(graph, start, end, visited, weight)

# 최대 무게 찾기
def find_max_weight(n, bridges, start, end):
    A = [[] for _ in range(n + 1)]

    min_weight = float('inf')
    max_weight = 0

    for a, b, c in bridges:
        A[a].append((b, c))
        A[b].append((a, c))
        min_weight = min(min_weight, c)
        max_weight = max(max_weight, c)

    left = min_weight
    right = max_weight
    result = min_weight

    while left <= right:
        mid = (left + right) // 2

        if can_transport_with_weight(A, start, end, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

# 입력 받기
n, m = map(int, input().split())
bridges = [tuple(map(int, input().split())) for _ in range(m)]
start, end = map(int, input().split())

# 최대 무게 출력
print(find_max_weight(n, bridges, start, end))