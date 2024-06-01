n = int(input())
log_list = [input() for _ in range(n)]

m = int(input())
A = [input() for _ in range(m)]

for i in range(n):
    if log_list[i] == '?':

        # ? 가 첫 단어로 올 경우
        if i == 0:
            if n > 2:
                next_word = log_list[i + 1]
                for candidate in A:
                    if candidate[-1] == next_word[0] and candidate not in log_list:
                        print(candidate)
                        break
            else:
                for candidate in A:
                    if candidate not in log_list:
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