import sys
input = sys.stdin.readline

# 딕셔너리에 {과일: 개수} 형태로 저장 후 동일한 과일이 들어올 때마다 cnt++
# cnt의 합에 따라 정답 출력(values())

n = int(input())
fruit_cnt = {}  # {과일: 개수} 형태의 딕셔너리

for _ in range(n):
    fruit, cnt = input().split()
    cnt = int(cnt)

    if fruit in fruit_cnt:
        fruit_cnt[fruit] += cnt
    else:
        fruit_cnt[fruit] = cnt

print('YES' if 5 in fruit_cnt.values() else 'NO')