# 등수 = 자신보다 더 잘한 국가의 수 + 1

n, m = map(int, input().split()) # 국가의 수, 등수를 알고 싶은 국가
medals = [list(map(int, input().split())) for _ in range(n)] # 국가별 메달 수
medals.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True) # 금은동 메달을 튜플로 반환 후 내림차순 정렬

rank = 1
target_rank = 0

for i in range(n):
    # 이전 국가와 메달 수가 다른 경우 rank update
    if i > 0 and (medals[i][1], medals[i][2], medals[i][3]) != (medals[i-1][1], medals[i-1][2], medals[i-1][3]):
        rank = i + 1

    # 등수를 알고 싶은 국가 찾기
    if medals[i][0] == m:
        target_rank = rank
        break

print(target_rank)