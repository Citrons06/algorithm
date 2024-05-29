# 전공평점 = sum(학점 * 과목평점) / 학점의 총합
# P/F 과목은 제외하고 계산

# 과목평점
rating = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

sum_rgt = 0
sum_score = 0
for i in range(20):
    sub, score, rgt = input().split() # 과목명, 학점, 등급

    # P/F 과목은 무시
    if rgt == 'P':
        continue

    sum_rgt += float(score) * rating[rgt] # sum(학점 * 과목평점)
    sum_score += float(score) # 학점의 총합

print(sum_rgt / sum_score)