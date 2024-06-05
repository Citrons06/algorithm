t = int(input())

for _ in range(t):
    s = str(input())
    stack = []
    ans = True

    for i in s:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if stack:
                stack.pop()
            else:
                ans = False
                break

    if ans and not stack:
        print('YES')
    else:
        print('NO')
