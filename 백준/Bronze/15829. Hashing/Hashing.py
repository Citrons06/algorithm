import sys
input = sys.stdin.readline

def cal_hash(data, r, M):
    H = 0
    for i in range(l):
        H = (H + data[i] * (r ** i)) % M
    return H

l = int(input().strip())
s = str(input().strip())

data = [ord(char) - ord('a') + 1 for char in s]

print(cal_hash(data, 31, 1234567891))
