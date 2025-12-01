data = open('data/day_6.txt').read().splitlines()

path = set()
x = y = -1
for idx, line in enumerate(data):
    pos = line.find("^")
    if pos != -1:
        x, y = pos, idx

data = [list(i) for i in data]
rotation = [[-1, 0], [0, 1], [1, 0], [0, -1]]
start_x, start_y = x, y


def in_bounds(x_pos, y_pos):
    return 0 < y_pos < len(data) - 1 and 0 < x_pos < len(data[0]) - 1


def is_loop_if_box(box_x, box_y):
    x, y = start_x, start_y
    positions = set()
    current_rotation = 0
    data[box_y][box_x] = "#"

    while in_bounds(x, y):
        dy, dx = rotation[current_rotation]

        while in_bounds(x, y) and data[y + dy][x + dx] != "#":
            x += dx
            y += dy
            if (y, x, current_rotation) in positions:
                data[box_y][box_x] = "."
                return True
            else:
                positions.add((y, x, current_rotation))

        current_rotation = (current_rotation + 1) % 4
    data[box_y][box_x] = "."
    return False


loops = 0
loop_checked = set()
current_rotation = 0
while in_bounds(x, y):
    dy, dx = rotation[current_rotation]

    # Path traversal
    while in_bounds(x, y) and data[y + dy][x + dx] != "#":
        path.add((x,y))
        x += dx
        y += dy

        # Loop checking
        if (y, x) not in loop_checked:
            if is_loop_if_box(x, y):
                loops += 1
            loop_checked.add((y, x))

    current_rotation = (current_rotation + 1) % 4

sums = len(path)
print(sums)
print(loops)
