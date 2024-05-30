n = int(input())
l_dic = {} # 사용자: 로그

for i in range(n):
    name, log = map(str, input().split()) # 사용자, 로그 입력
    # 사용자 value 에 log 기록, enter 이후에 leave 로그가 찍히면 값이 leave로 덮어 씌워지는 걸 이용
    l_dic[name] = log

    # value 값이 leave 가 된 사용자 딕셔너리에서 제거
    if l_dic[name] == 'leave':
        del l_dic[name]

#이름을 기준으로 내림차순 정렬
key = sorted(l_dic.keys(), reverse=True)

for i in key:
    print(i)