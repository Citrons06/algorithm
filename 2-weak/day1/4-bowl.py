import sys
input = sys.stdin.readline

bowl = str(input())

# ! 현재 인덱스의 값과 이전 인덱스의 값이 동일하면 +5cm, 동일하지 않으면 +10cm

h = 0  # 그릇의 높이
for i in range(1, len(bowl)):
    if bowl[i] == bowl[i-1]:
        h += 5
    if bowl[i] != bowl[i-1]:
        h += 10

print(h)