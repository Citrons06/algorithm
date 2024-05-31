n = int(input())
a = [0] * n

for i in range(n):
    a[i] = int(input())

stack = []
num = 1
result = True
answer = ''

for i in range(n):
    su = a[i]

    # 현재 수열 값 >= 오름차순 자연수
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            answer += '+\n'
        stack.pop()
        answer += '-\n'

    # 현재 수열 값 < 오름차순 자연수
    else:
        n = stack.pop()

        # 스택의 가장 위의 수가 만들어야 하는 수열의 수보다 크면 수열 출력 불가능
        if n > su:
            print('NO')
            result = False
            break
        else:
            answer += '-\n'

if result:
    print(answer)