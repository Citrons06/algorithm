# 해시 테이블 생성
hash_table = {}

# 삽입
hash_table['apple'] = '사과'
hash_table['banana'] = '바나나'
hash_table['grape'] = '포도'

print('현재 해시 테이블:', hash_table) # {'apple': '사과', 'banana': '바나나', 'grape': '포도'}

# 검색
print('apple의 값:', hash_table['apple']) # 사과
print('banana의 값:', hash_table['banana']) # 바나나

# 삭제
del hash_table['grape']
print('현재 해시 테이블:', hash_table) # {'apple': '사과', 'banana': '바나나'}