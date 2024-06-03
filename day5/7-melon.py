n = int(input())
s = [list(map(int, input().split())) for _ in range(6)] # 방향, 거리 리스트
l = []
h = []
small = []


for i in range(6):
    if s[i][0] == 1 or s[i][0] == 2:
        l.append(s[i][1])  # 가로
    if s[i][0] == 3 or s[i][0] == 4:
        h.append(s[i][1])  # 세로

for i in range(6):
    if s[i][0] == s[(i + 2) % 6][0]:
        small.append(s[(i + 1) % 6][1])  # 작은 사각형의 가로/세로 길이 찾기

print(((max(l) * max(h)) - (small[0] * small[1])) * n)