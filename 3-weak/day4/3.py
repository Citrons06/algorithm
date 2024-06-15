def decrease_numbers(n, A):
    dp = [1] * n

    # dp[i] = i번째 원소를 사용한 0~i까지 찾은 가장 긴 감소하는 부분 수열의 길이
    for i in range(1, n):
        for j in range(i):
            if A[j] > A[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # dp 테이블에서 가장 큰 값 찾음

n = int(input())
A = list(map(int, input().split()))

print(decrease_numbers(n, A))