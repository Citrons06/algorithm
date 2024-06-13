def cal_min_square(min_x, max_x, min_y, max_y):
    return (max_x - min_x) * (max_y - min_y)

t = int(input())
control = [input().strip() for _ in range(t)]

for con in control:
    x, y = 0, 0
    looking = 0
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    min_x = max_x = x
    min_y = max_y = y

    for cmd in con:
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

        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    print(cal_min_square(min_x, max_x, min_y, max_y))