s = str(input())

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for croa in croatia:
    # 문자열에 croatia 알파벳이 있으면 'c'로 대체
    s = s.replace(croa, 'c')

print(len(s))
