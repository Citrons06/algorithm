t = int(input())

for _ in range(t):
    n = int(input())  # 학교의 숫자

    school = {}
    for _ in range(n):
        school_name, con_alcohol = input().split()
        con_alcohol = int(con_alcohol)
        school[school_name] = con_alcohol

    # 술 소비가 가장 많은 학교의 이름
    sort_school = sorted(school, key=lambda x: x[1], reverse=True)
    print(sort_school[-1])