n = int(input())
sold_out_num = list(map(int, input().split()))

check = {}
for sold in sold_out_num:
    check[sold] = 1

ticket_num = []
for i in range(1, max(sold_out_num) + 2):
    ticket_num.append(i)

for ticket in ticket_num:
    if check.get(ticket, 0) == 0:
        print(ticket)
        break