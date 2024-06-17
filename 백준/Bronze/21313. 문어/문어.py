n = int(input())

A = [1, 2] * (n // 2) + ([3] if n % 2 else [])
print(*A)