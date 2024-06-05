s = str(input())

list = []
idx = 0 # 시작 인덱스

# [0] ~ [len(s)], [1] ~ [len(s)], [2] ~ [len(s)] ... 흐름으로 탐색
while idx <= len(s):

    for i in range(idx, len(s)):
        list.append(s[idx : i + 1]) # 모든 경우의 문자열 list에 저장

    idx += 1 # 시작 인덱스 값 증가시킴

set_list = set(list) # 리스트의 중복 제거
print(len(set_list))