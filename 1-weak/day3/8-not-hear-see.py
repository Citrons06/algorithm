n, m = map(int, input().split())
list = []

for i in range(n + m):
    a = str(input())
    list.append(a)

# 듣보 사람들 한꺼번에 리스트에 추가하고 못 들어본 사람 수 기준 슬라이싱
h_list = list[:n]
s_list = list[n:]

# 중복된 사람들 확인 (시간 초과)
# common_list = [common for common in h_list if common in s_list]

# set.intersection() 이용해서 공통 요소 찾기
h_set = set(h_list)
s_set = set(s_list)
common_set = sorted(h_set.intersection(s_set))

print(len(common_set), *common_set, sep='\n')

# 45492KB 3876ms