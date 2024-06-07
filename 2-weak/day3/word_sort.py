from collections import defaultdict

n = int(input())
len_word_mapper = defaultdict(set)  # 중복 제거
for _ in range(n):
    word = input()
    # 같은 길이를 가진 단어들끼리 한 셋에 묶임
    len_word_mapper[len(word)].add(word)  # {3: {'but'}, 1: {'i'}, 4: {'wont', 'wait', 'more'}}

keys = list(len_word_mapper.keys())  # 단어가 짧은 순으로 정렬
keys.sort()
for key in keys:
    words = list(len_word_mapper[key])
    words.sort()
    for word in words:
        print(word)