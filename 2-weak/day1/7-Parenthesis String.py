# 올바른 괄호 문자열(VPS): ( ) 양 괄호가 대칭으로 이루어져 있는 괄호
# (()()) ((()))
t = int(input())  # 입력 데이터 수

# ! 스택 이용
# ! 기본적으로 처음 들어온 문자가 '(' 이면 append(), ')' 이면 pop()
for _ in range(t):
    s = str(input())  # 괄호 문자열 입력
    stack = []
    ans = True  # VPS 여부 판단

    for i in s:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if stack:  # 스택에 '('이 있으면 '(' 제거
                stack.pop()
            else:  # 스택에 '('이 없으면 VPS가 아님, 바로 종료
                ans = False
                break

    if ans and not stack:  # 스택이 비어있고, VPS인 경우
        print('YES')
    else:  # VPS가 아닌 경우
        print('NO')
