members = []
for _ in range(3):
    solve, years, name = input().split()
    solve = int(solve)
    members.append((solve, years, name))

# 입학 연도를 100으로 나눈 나머지를 오름차순 정렬로 이어 붙임
sorted_members = sorted(members, key=lambda x: x[1])
name_year = ''
for i in range(3):
    name_year += sorted_members[i][1][2:5]
print(name_year)

# 해결 문제가 많은 사람의 성씨를 차례대로 나열
sur_name = ''
sorted_members = sorted(members, key=lambda x: x[0], reverse=True)
for i in range(3):
    sur_name += sorted_members[i][2][:1]
print(sur_name)