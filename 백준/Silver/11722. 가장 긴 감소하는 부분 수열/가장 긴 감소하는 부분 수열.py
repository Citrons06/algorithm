def decrease_numbers(n, A):
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if A[j] > A[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

n = int(input())
A = list(map(int, input().split()))

print(decrease_numbers(n, A))