checkList = [0] * 4 # 비밀번호 체크 리스트
myList = [0] * 4 # 현재 문자열 상태 리스트, ['A', 'C', 'G', 'T']
checkSecret = 0 # 몇 개의 문자와 관련된 개수를 충족했는지 판단하는 변수

# 문자 c를 부분 문자열에 추가할 때 myList 업데이트
# checkList 조건을 새롭게 만족하게 되면 checkSecret 1 증가
def myadd(c):
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

# 문자 c를 부분 문자열에서 제거할 때 myList 업데이트
# checkList 조건을 더 이상 만족하지 않으면 checkSecret 1 감소
def myremove(c):
    global checkList, myList, checkSecret

    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

s, p = map(int, input().split())
result = 0
A = list(input())
checkList = list(map(int, input().split()))

# 부분 문자열에 없어도 되는 경우 조건을 만족한 것으로 간주
for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

for i in range(p):
    myadd(A[i])

# 모든 자릿수가 충족되는 문자열인 경우
if checkSecret == 4:
    result += 1

# 부분 문자열을 한 문자 씩 이동시키면서 조건을 만족하는지 확인
# i: 윈도우의 마지막 문자
# j = i - p: 윈도우가 이동함에 따라 제거될 문자의 인덱스
for i in range(p, s):
    j = i - p
    myadd(A[i]) # 새로운 문자 추가
    myremove(A[j]) # 가장 앞의 문자 제거
    if checkSecret == 4:
        result += 1

print(result)