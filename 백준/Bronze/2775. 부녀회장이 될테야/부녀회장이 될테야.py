def fib(k, n, memo):
    if k == 0:
        return n
    if n == 1:
        return 1
    
    if (k, n) in memo:
        return memo[(k, n)]

    memo[(k, n)] = fib(k - 1, n, memo) + fib(k, n - 1, memo)
    return memo[(k, n)]

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())

    memo = {}
    print(fib(k, n, memo))