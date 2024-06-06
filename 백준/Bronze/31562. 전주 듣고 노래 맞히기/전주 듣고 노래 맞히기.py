import sys

input = sys.stdin.readline

n, m = map(int, input().split())

songs = []
for _ in range(n):
    t, s, *a = input().split()
    t = int(t)
    songs.append((t, s, a))

notes = [input().strip().split() for _ in range(m)]

check = {}
for song in songs:
    check[song[1]] = song[2][:3]

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