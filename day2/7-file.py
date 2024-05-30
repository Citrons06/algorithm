n = int(input()) # 파일의 개수
ext = []
e_dic = {}

for i in range(n):
    file = str(input()) # 파일명.확장자
    ext.append(file.split('.')[1]) # 파일명과 확장자를 분리하고 확장자를 ext 리스트에 저장

for i in ext:

    # 딕셔너리에 해당 확장자가 이미 존재하면 +1
    if i in e_dic:
        e_dic[i] += 1
    # 닥셔너리에 해당 확장자가 없으면 1 세팅
    else:
        e_dic[i] = 1

# 확장자 이름 오름차순 정렬
e_sort = sorted(e_dic)

for e in e_sort:
    print(e + ' ' + str(e_dic[e]))