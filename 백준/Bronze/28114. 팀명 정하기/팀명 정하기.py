members = []
for _ in range(3):
    solve, years, name = input().split()
    solve = int(solve)
    members.append((solve, years, name))

sorted_members = sorted(members, key=lambda x: x[1])
name_year = ''
for i in range(3):
    name_year += sorted_members[i][1][2:5]
print(name_year)

sur_name = ''
sorted_members = sorted(members, key=lambda x: x[0], reverse=True)
for i in range(3):
    sur_name += sorted_members[i][2][:1]
print(sur_name)