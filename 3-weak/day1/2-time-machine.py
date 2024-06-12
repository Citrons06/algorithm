from itertools import permutations

# permutations로 가능한 조합을 생성하고, 유효한 시간인지 확인

# 각 시, 분, 초 범위 안에 있는지 확인
def val_time(h, m, s):
    return 1 <= h <= 12 and 0 <= m <= 59 and 0 <= s <= 59

def find_time_combi(h, m, s):

    cnt = 0
    # 가능한 모든 조합 생성 후
    for per in permutations(times):
        h, m, s = per

        # 각 시간이 유효한 범위 안에 있을 때마다 cnt++
        if val_time(h, m, s):
            cnt += 1

    return cnt

times = list(map(int, input().split(':')))

# 읽을 수 있는 시간 구하기
print(find_time_combi(*times))