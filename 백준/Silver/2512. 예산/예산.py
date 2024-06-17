def solution(local_budget, total_budget):
    if sum(local_budget) <= total_budget:
        return max(local_budget)

    local_budget.sort()
    left = 0
    right = max(local_budget)

    while left <= right:
        mid = (left + right) // 2
        cur_total = sum(min(budget, mid) for budget in local_budget)

        if cur_total <= total_budget:
            left = mid + 1
        else:
            right = mid - 1

    return right

n = int(input())
local = list(map(int, input().split()))
total_budget = int(input())

print(solution(local, total_budget))

