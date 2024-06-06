import sys

input = sys.stdin.readline

# n: 정환이 아는 노래의 수, m: 정환이 시도할 노래의 수
n, m = map(int, input().split())

songs = []  # 노래 리스트 [[t, s, a], ,,,]
for _ in range(n):
    # t: 제목의 길이, s: 노래 제목, a: 음 이름 일곱 개
    t, s, *a = input().split()
    t = int(t)
    songs.append((t, s, a))

# 정환이가 시도할 첫 세 음
notes = [input().strip().split() for _ in range(m)]

# {노래 제목: 첫 세 음} 형태로 저장
check = {}
for song in songs:
    check[song[1]] = song[2][:3]

# a의 첫 세 음과 note의 일치 여부 판단
# ! 노래의 첫 세 음과 정환이가 시도할 첫 세 음이 일치할 때마다 cnt++
# ! cnt 값에 따라 출력
for note in notes:
    cnt = 0
    song_name = ''

    for song, no in check.items():
        if note == no:
            cnt += 1
            song_name = song

    if cnt >= 2:
        print('?')
    if cnt == 1:
        print(song_name)
    if cnt == 0:
        print('!')