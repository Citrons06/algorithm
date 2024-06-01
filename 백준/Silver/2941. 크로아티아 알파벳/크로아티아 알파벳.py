s = str(input())

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0

for croa in croatia:
    s = s.replace(croa, 'c')

print(len(s))