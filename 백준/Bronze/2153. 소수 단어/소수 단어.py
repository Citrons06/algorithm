import sys
input = sys.stdin.readline

word = input().strip()

total = 0
for i in range(len(word)):

    if word[i].islower():
        total += ord(word[i]) - 96
    else:
        total += ord(word[i]) - 38

def isPrime(n):
    for i in range(2, int(n ** (0.5) + 1)):
        if n % i == 0:
            return 'It is not a prime word.'
    return 'It is a prime word.'

print(isPrime(total))