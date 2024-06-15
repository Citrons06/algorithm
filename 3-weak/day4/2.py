# 피보나치 수열
# 메모이제이션을 이용해서 계산한 결과 저장
def fib(k, n, memo):
    if k == 0:
        return n
    if n == 1:
        return 1

    # memo에 이미 계산된 값이 있으면 바로 반환
    if (k, n) in memo:
        return memo[(k, n)]

    # memo에 (k, n)이 없으면 재귀 호출해서 계산, 결과 반환
    memo[(k, n)] = fib(k - 1, n, memo) + fib(k, n - 1, memo)
    return memo[(k, n)]

t = int(input())
for _ in range(t):
    k = int(input())  # 층
    n = int(input())  # 호

    memo = {}
    print(fib(k, n, memo))