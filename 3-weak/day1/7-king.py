king, stone, n = map(str, input().split())
n = int(n)
moves = [str(input()) for _ in range(n)]

# 이동 방향
move_dic = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (-1, 0),
    'T': (1, 0),
    'RT': (1, 1),
    'LT': (1, -1),
    'RB': (-1, 1),
    'LB': (-1, -1)
}

# 체스 좌표 -> 행렬 좌표 변환: A1 -> (7, 0)
def pos_to_indices(pos):
    return (int(pos[1]) - 1, ord(pos[0]) - ord('A'))

# 행렬 좌표 -> 체스 좌표 변환
def indices_to_pos(indices):
    return chr(indices[1] + ord('A')) + str(8 - int(indices[0]))

king_pos = pos_to_indices(king)
stone_pos = pos_to_indices(stone)

for move in moves:
    move_vec = move_dic[move]

    new_king_pos = (king_pos[0] + move_vec[0], king_pos[1] + move_vec[1])

    # 이동한 킹의 위치가 체스판 내에 있는가?
    if 0 <= new_king_pos[0] < 8 and 0 <= new_king_pos[1] < 8:
        # 킹이 이동한 곳에 돌이 있는가? -> 돌도 같은 방향으로 이동
        if new_king_pos == stone_pos:
            new_stone_pos = (stone_pos[0] + move_vec[0], stone_pos[1] + move_vec[1])

            # 이동한 킹과 돌의 위치 모두 체스판 내에 있으면 pos 갱신
            if 0 <= new_stone_pos[0] < 8 and 0 <= new_stone_pos[1] < 8:
                stone_pos = new_stone_pos
                king_pos = new_king_pos

        else:
            king_pos = new_king_pos

print(indices_to_pos(king_pos))
print(indices_to_pos(stone_pos))