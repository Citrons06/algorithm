from itertools import combinations

n = int(input())
scoreboard = [list(map(int, input().split())) for _ in range(n)]

team_with_0s = list(combinations(range(1, n), n // 2 - 1))  # 0번 사람 + 절반-1 으로 팀 구성
m = float('inf')  # 무한대 - 최솟값을 찾을 때 초깃값으로 세팅하면 편함

for team1 in team_with_0s:
    team1 = [0] + list(team1)
    team2 = list(set(range(n)) - set(team1))  # 2번째 팀은 1번째 팀에 속하지 않는 사람들로 구성
    score1 = 0
    score2 = 0

    for i in range(n // 2):
        for j in range(n // 2):
            score1 += scoreboard[team1[i]][team2[i]]
            score2 += scoreboard[team1[i]][team2[i]]
    m = min(m, abs(score1 - score2))

print(m)