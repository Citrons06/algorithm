x = int(input())
line = 1 # 지그재그 순으로 정렬한 배열의 라인 수

# 몇 번째 라인의 몇 번째 칸에 있는지 탐색
# line: 라인 수 / x = 칸
while x > line:
    x -= line
    line += 1

# 짝수인 경우 - 분자 = 칸
if line % 2 == 0:
    a = x
    b = line - x + 1 # ?

# 홀수인 경우 - 분모 = 칸
elif line % 2 == 1:
    a = line - x + 1
    b = x

print (f'{a}/{b}')