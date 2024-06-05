a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

# f(n) <= c * n
# 결국 a1*n과 c*n을 비교하는 것, a1 > c의 경우 반례 발생
if a1 * n + a0 <= c * n and a1 <= c:
    print(1)
else:
    print(0)

#31120KB, 48ms