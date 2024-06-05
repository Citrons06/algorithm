n = int(input()) # 카드의 개수
fruit_count = {} # 과일: 개수 형태의 딕셔너리

for _ in range(n):
    fruit, count = input().split() # 과일 이름, 과일 수
    count = int(count)

    # 딕셔너리에 과일이 존재하면 +count, 없으면 count 세팅
    if fruit in fruit_count:
        fruit_count[fruit] += count
    else:
        fruit_count[fruit] = count

# 딕셔너리의 key가 5면 YES, 아니면 NO 출력
print('YES' if 5 in fruit_count.values() else 'NO')