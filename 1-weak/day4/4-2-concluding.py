n = int(input())
log_list = []

for i in range(n):
    log_list.append(input())

m = int(input())
A = []

for i in range(m):
    A.append(input())

if '?' in log_list:

    i = log_list.index('?') # '?' 위치 인덱스

    if i == 0:
        first_char = '' # 앞 문자가 없으므로 빈 값 세팅
    else:
        first_char = log_list[i - 1][-1]

    if i == len(log_list) - 1:
        last_char = '' # 다음 문자가 없으므로 빈 값 세팅
    else:
        last_char = log_list[i + 1][0]

    for candidate in A:
        if candidate not in log_list:
            if (not first_char or candidate[0] == first_char) and (not last_char or candidate[-1] == last_char):
                print(candidate)