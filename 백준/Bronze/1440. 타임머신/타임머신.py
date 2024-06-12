from itertools import permutations

def val_time(h, m, s):
    return 1 <= h <= 12 and 0 <= m <= 59 and 0 <= s <= 59

def find_time_combi(h, m, s):

    cnt = 0
    for per in permutations(times):
        h, m, s = per
        
        if val_time(h, m, s):
            cnt += 1

    return cnt

times = list(map(int, input().split(':')))

print(find_time_combi(*times))