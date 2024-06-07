t = int(input())

for _ in range(t):
    n = int(input())  # 학교의 숫자

    school = {}  # {학교의 이름: 술 소비량}
    for _ in range(n):
        school_name, con_alcohol = input().split()
        con_alcohol = int(con_alcohol)
        school[school_name] = con_alcohol

    # 술 소비량을 기준으로 내림차순 정렬 후 마지막 학교 이름 출력
    sort_school = sorted(school, key=lambda x: x[1], reverse=True)
    print(sort_school[-1])