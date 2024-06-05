s = input().upper() # 대소문자 구별을 없애기 위해 모두 대문자로 변환
s_dic = {}

for i in s:
    # 각 문자의 수를 딕셔너리 value에 update
    if i in s_dic:
        s_dic[i] += 1
    else:
        s_dic[i] = 1

max_freq = max(s_dic.values()) # 가장 많이 등장한 문자의 빈도 수
# max 빈도에 해당하는 문자들을 찾아 리스트에 저장
max_char = [char for char, freq in s_dic.items() if freq == max_freq]

print(max_char[0]) if len(max_char) == 1 else print('?')