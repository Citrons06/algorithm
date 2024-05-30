# 두 수를 string 으로 받고 뒤집은 후에 int 형변환 해서 비교
a, b = map(str, input().split())

print(int(a[::-1])) if int(a[::-1]) > int(b[::-1]) else print(int(b[::-1]))