n = int(input()) # 채팅방 기록 수
emt = set()
cnt = 0

for i in range(n):
    log = str(input())

    # ENTER log가 들어오면 set.clear()
    if log == 'ENTER':
        emt.clear()
        emt.add(log)

    # ENTER 이후 새로운 log가 들어오면 cnt++
    elif log not in emt:
        cnt += 1
        emt.add(log)

print(cnt)

# 42388KB 3888ms