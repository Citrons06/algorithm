import sys
input = sys.stdin.readline

# ! 단어의 합을 구하고(ord() 이용) 에라토스 테네스의 체로 소수 판별
word = input().strip()

# ord() = {a: 97, b:98, c: 99, ..., z: 122, ... , A: 65, B: 66, C: 67, ... , Z: 90}
# 임의 설정 = {a: 1, b: 2, c: 3, ... , A: 27, B: 28, C: 29, ... , Z: 52}
# 소문자는 96, 대문자는 38 만큼의 차이

# 단어의 합 구하기
total = 0
for i in range(len(word)):
    # 해당 글자가 소문자일 경우
    if word[i].islower():
        total += ord(word[i]) - 96
    # 해당 글자가 대문자일 경우
    else:
        total += ord(word[i]) - 38

# 소수 판별
def isPrime(n):
    for i in range(2, int(n ** (0.5) + 1)):
        # 나누어 떨어지는 수가 있으므로 소수가 아님
        if n % i == 0:
            return 'It is not a prime word.'
    # 나누어 떨어지는 수가 없으므로 소수임
    return 'It is a prime word.'

print(isPrime(total))