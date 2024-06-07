# 1부터 시작하는 티켓의 번호들 중 이미 팔린 티켓 번호를 제외한 가장 작은 수
n = int(input())
sold_out_num = list(map(int, input().split()))

check = {}  # 팔린 번호 표시 {4: 1, 1: 1, 2: 1, ...}
for sold in sold_out_num:
    check[sold] = 1

# all 티켓 번호 리스트
# 1 ~ max(sold_out_num) + 2: [1, 2, 3] 처럼 팔린 번호가 누락 없이 연달아 오는 경우를 위함
ticket_num = []
for i in range(1, max(sold_out_num) + 2):
    ticket_num.append(i)

# all 티켓 리스트로 팔린 티켓 번호 검색
# 딕셔너리 get() 함수로 팔린 티켓 번호에 누락된 번호가 있으면 0 세팅
for ticket in ticket_num:
    if check.get(ticket, 0) == 0:  # 0으로 가져오면 아직 팔리지 않은 티켓 번호인 것
        print(ticket)
        break