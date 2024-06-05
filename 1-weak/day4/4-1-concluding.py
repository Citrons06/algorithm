n = int(input())
log_list = []

for i in range(n):
    log_list.append(input())

m = int(input())
A = []

for i in range(m):
    A.append(input())

for i in range(n):
    if log_list[i] == '?':

        # ? 가 첫 단어로 올 경우
        if i == 0:
            if n == 1:  # ? 만 들어오는 경우
                for candidate in A:
                    print(candidate)
                    break

            else:
                next_word = log_list[i + 1]
                for candidate in A:
                    if candidate[-1] == next_word[0] and candidate not in log_list:
                        print(candidate)

        # ? 가 중간에 올 경우
        elif i < len(log_list) - 1:
            next_word = log_list[i + 1]
            for candidate in A:
                if candidate[0] == log_list[i - 1][-1] and candidate[-1] == next_word[0] and candidate not in log_list:
                    print(candidate)
                    break

        # ? 가 마지막으로 올 경우
        elif i == n - 1:
            for candidate in A:
                if candidate[0] == log_list[i - 1][-1] and candidate not in log_list:
                    print(candidate)

### 계속 테스트 케이스에서 틀렸다고 뜨는데 반례를 모르겠음 ... ###