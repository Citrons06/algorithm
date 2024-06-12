word = str(input())

divided_words = []

# 이중 for문으로 단어를 세 부분으로 나누는 모든 경우의 수를 수행하고 각각 뒤집어서 리스트에 저장
for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        part1 = word[:i][::-1]
        part2 = word[i:j][::-1]
        part3 = word[j:][::-1]
        divided_words.append(part1 + part2 + part3)

print(min(divided_words))  # 사전순으로 가장 앞에 있는 단어