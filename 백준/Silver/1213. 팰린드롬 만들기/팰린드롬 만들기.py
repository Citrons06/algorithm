from collections import Counter

s = sorted(str(input()))

char_cnt = Counter(s)
ans = [''] * len(s)

left = 0
right = len(s) - 1

odd_char = ''
odd_cnt = 0

for char, cnt in char_cnt.items():
    if cnt % 2 != 0:
        odd_cnt += 1
        odd_char = char

if odd_cnt > 1:
    print("I'm Sorry Hansoo")

else:
    for char, cnt in char_cnt.items():
        if cnt % 2 == 0:
            ans[left : left + cnt // 2] = char * (cnt // 2)
            ans[right + 1 - (cnt // 2) : right + 1] = char * (cnt // 2)

        else:
            ans[left : left + cnt // 2] = char * (cnt // 2)
            ans[right + 1 - (cnt // 2) : right + 1] = char * (cnt // 2)
            ans[len(s) // 2] = char
        left += cnt // 2
        right -= cnt // 2

print(''.join(ans))