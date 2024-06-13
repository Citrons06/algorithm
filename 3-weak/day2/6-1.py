def cal_min_square(position):
    min_x = min(pos[0] for pos in position)
    max_x = max(pos[0] for pos in position)
    min_y = min(pos[1] for pos in position)
    max_y = max(pos[1] for pos in position)

    return (max_x - min_x) * (max_y - min_y)

t = int(input())
control = [input().strip() for _ in range(t)]

for con in control:
    x, y = 0, 0
    looking = 0
    positions = [(x, y)]
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for cmd in control:
        if cmd == 'F':
            x += dir[looking][0]
            y += dir[looking][1]
        elif cmd == 'B':
            x -= dir[looking][0]
            y -= dir[looking][1]
        elif cmd == 'L':
            looking = (looking - 1) % 4
        elif cmd == 'R':
            looking = (looking + 1) % 4

        positions.append((x, y))

    area = cal_min_square(positions)
    print(area)