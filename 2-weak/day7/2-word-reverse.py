import sys
input = sys.stdin.readline

# ! 케이스 번호가 x일때 'Case #x: ' 출력 후 단어들을 반대 순서로 출력

n = int(input())
words = [str(input()) for _ in range(n)]  # 문장
word = [w.split() for w in words]  # 문장의 단어들

# 단어들을 거꾸로 출력
for i in range(n):
    print(f'Case #{i+1}:', *word[i][::-1])