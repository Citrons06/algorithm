n = int(input())
words = {input() for _ in range(n)}  # 중복 제거를 위해 set으로 생성
words = list(words)  # sort를 하기 위해 list로 변환
words.sort(key=lambda x: (len(x), x))  # 길이순으로 정렬 후, 길이가 같다면 사전 순으로 정렬
for word in words:
    print(word)