# --- 1 --- #
n = int(input()) # 과목 개수
grades = list(map(int, input().split())) # n개 과목들의 점수
trns_grades = [] # 바꾼 점수 리스트

# 점수 변환
for i in grades:
    i = (i / max(grades)) * 100

    trns_grades.append(i)

# 평균 구하기
print((100 * sum(trns_grades)) / (max(trns_grades) * len(trns_grades)))

# --- 2 --- #
n = int(input()) # 과목 개수
grades = list(map(int, input().split())) # n개 과목들의 점수

nmax = max(grades)
sum = sum(grades)

# 평균 구하기
print((sum * 100) / nmax / int(n))