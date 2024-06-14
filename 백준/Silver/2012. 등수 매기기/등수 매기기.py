import sys

input = sys.stdin.readline

def cal_dissatisfaction(expect_rank, n):
    dissatisfaction = 0

    for real_rank in range(1, n+1):
        dissatisfaction += abs(real_rank - expect_rank[real_rank - 1])

    return dissatisfaction

n = int(input())
expect_rank = [int(input()) for _ in range(n)]
expect_rank.sort()

print(cal_dissatisfaction(expect_rank, n))