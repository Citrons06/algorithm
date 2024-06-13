from collections import Counter

hansoo = sorted(str(input()))

char_cnt = Counter(hansoo)
ans = [''] * len(hansoo)

left = 0
right = len(hansoo) - 1

odd_char = ''
odd_cnt = 0

for char, cnt in char_cnt.items():
    if cnt % 2 != 0:
        odd_cnt += 1
        odd_char = char

if odd_cnt > 1: # 홀수 빈도 > 1: 팰린드롬 불가능
    print("I'm Sorry Hansoo")

else:
    for char, cnt in char_cnt.items():
        if cnt % 2 == 0:
            ans[left : left + cnt // 2] = char * (cnt // 2)
            ans[right + 1 - (cnt // 2) : right + 1] = char * (cnt // 2)

        else:
            # 홀수 빈도 문자의 경우 중앙에 배치 후 나머지 문자들은 양쪽에 분배
            # 오름차순 정렬을 위함
            ans[len(hansoo) // 2] = char
            ans[left : left + cnt // 2] = char * (cnt // 2)
            ans[right + 1 - (cnt // 2) : right + 1] = char * (cnt // 2)
        left += cnt // 2
        right -= cnt // 2

print(''.join(ans))