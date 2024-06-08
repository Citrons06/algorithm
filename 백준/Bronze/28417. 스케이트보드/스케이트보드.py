n = int(input())

run_score = []
trick_score = []
for _ in range(n):
    score = list(map(int, input().split()))
    run_score.append(sorted(score[:2], reverse=True))
    trick_score.append(sorted(score[2:7], reverse=True))

total_score = []
for i in range(len(trick_score)):
    total_score.append(run_score[i][0] + trick_score[i][0] + trick_score[i][1])

print(max(total_score))
