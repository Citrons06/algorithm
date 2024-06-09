s = str(input())

left = 0
right = 0
for bracket in s:

    if bracket == '(':
        left += 1

    if bracket == ')':
        if left > 0:
            left -= 1
        else:
            right += 1

print(left + right)