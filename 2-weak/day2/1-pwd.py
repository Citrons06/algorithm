import sys
input = sys.stdin.readline

# 비밀번호: 파일 내에 뒤집은 문자열이 있는 문자열

n = int(input())
pwd = [str(input().rstrip()) for _ in range(n)]
check = {}

# ! 해시 테이블의 키에 비밀번호를 저장하고
# ! 뒤집은 비밀번호가 해시 테이블의 키 리스트에 있는지 확인
for p in pwd:
    check[p] = 1

    if p[::-1] in check.keys():
        print(len(p) ,p[len(p) // 2])