import sys
from collections import deque
input = sys.stdin.readline

# ! 덱 이용
# ! 문서 출력 전에 중요도를 확인하고 popleft() or 맨 뒤로 재배치(X.append(X.popleft())
# 타겟 문서가 들어올 때까지 카운트

t = int(input())  # 테스트 케이스의 수
for i in range(t):
    n, m = map(int, input().split())  # n: 문서의 개수, m: 타겟 문서의 위치
    imp = deque(list(map(int, input().split())))  # 중요도(1~9)

    doc = deque([i for i in range(n)])  # 문서 순서 저장 리스트
    cnt = 0  # 현재 출력된 문서 수

    # 문서를 돌면서 중요도가 높은 순으로 출력 처리(popleft())
    while doc: # 문서가 출력되는 동안
        # 가장 중요한 문서가 들어오면 출력 및 cnt++
        if imp[0] == max(imp):
            cnt += 1
            imp.popleft()
            if doc.popleft() == m:  # 타겟 문서가 출력되면
                print(cnt)          # 출력된 문서 수를 리턴하고 종료
                break
        else:
            # 들어온 문서의 중요도가 가장 높지 않으면 맨 오른쪽으로 재배치
            imp.append(imp.popleft())
            doc.append(doc.popleft())