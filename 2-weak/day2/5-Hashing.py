import sys
input = sys.stdin.readline

# 문자열 s = sum(((ord(s[i]) - ord('a') + 1) * (31 ** i)) % 1234567891)

def cal_hash(data, r, M):
    H = 0
    for i in range(l):
        H = (H + data[i] * (r ** i)) % M
    return H

l = int(input().strip())
s = str(input().strip())

data = [ord(char) - ord('a') + 1 for char in s]  # 문자열을 고유 번호로 변환

print(cal_hash(data, 31, 1234567891))