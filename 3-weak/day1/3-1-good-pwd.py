# 소인수분해를 진행하면서 factors 리스트에 인수 담기
def factorization(k):
    factors = []
    i = 2

    while i * i <= k:  # 소수의 특성상 제곱근까지만 검사해도 된다.
        if k % i == 0:
            factors.append(i)

            # 중복 소인수 제거 -> 동일한 소인수를 여러 번 나누는 과정 최적화
            while k % i == 0:
                k //= i

        i += 1

    if k > 1:
        factors.append(k)  # 남은 소인수 추가

    return factors

K, L = map(int, input().split())

factors = factorization(K)  # 소인수분해

if min(factors) == L:
    print('GOOD')
else:
    print('BAD', min(factors))