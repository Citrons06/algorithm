A = [input() for _ in range(5)]
max_len = max(len(line) for line in A)  # 가장 긴 문자열의 길이

ans = ''

for i in range(max_len):
    for line in A:
        # 인덱스가 현재 문자열 길이 안에 포함되어 있을 때에만 출력 문자열에 추가
        if i < len(line):
            ans += line[i]

print(ans)