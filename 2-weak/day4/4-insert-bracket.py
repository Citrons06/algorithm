s = str(input())

# ! 여는 괄호, 닫는 괄호의 개수가 일치하면 올바른 괄호

left = 0
right = 0
for bracket in s:

    if bracket == '(':
        left += 1

    if bracket == ')':
        # 여는 괄호가 1개 이상이면 left--
        if left > 0:
            left -= 1
        # 여는 괄호가 없으면 right++
        else:
            right += 1

print(left + right)