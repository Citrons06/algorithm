from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

# combinations로 카드 세 장을 뽑는 경우의 수 찾고
# m을 넘지 않는 숫자들의 합을 정답 리스트에 담아서
ans = []
for i in combinations(cards, 3):
    if sum(i) <= m:
        ans.append(sum(i))

# 최댓값 출력
print(max(ans))