from collections import deque


def move_boxes(direction: (int, int), robot: (int, int), warehouse, wide) -> (int, int):
    new_pos = warehouse[robot[1] + direction[1]][robot[0] + direction[0]]
    match new_pos:
        case 0:
            robot = (robot[0] + direction[0], robot[1] + direction[1])
        case 1 | 3:
            is_vertical = direction[1] != 0
            box_queue = deque()
            pointer = [robot[0] + direction[0], robot[1] + direction[1]]
            box_queue.append(pointer)
            real_move = True
            moves = set()
            while box_queue:
                pointer = box_queue.popleft()
                next_val = warehouse[pointer[1]][pointer[0]]
                moves.add((pointer[0], pointer[1], warehouse[pointer[1] - direction[1]][pointer[0] - direction[0]]))
                if next_val == -1:
                    real_move = False
                    break
                elif next_val == 0:
                    continue
                else:
                    if is_vertical:
                        box_queue.append([pointer[0], pointer[1] + direction[1]])
                        if wide:
                            if next_val == 1:  # left piece
                                box_queue.append([pointer[0] + 1, pointer[1] + direction[1]])
                            else:
                                box_queue.append([pointer[0] - 1, pointer[1] + direction[1]])
                    else:
                        box_queue.append([pointer[0] + direction[0], pointer[1]])
            if real_move:
                for move in sorted(moves, key=lambda x: (-x[0] * direction[0] + -x[1] * direction[1])):
                    warehouse[move[1]][move[0]] = move[2]
                    warehouse[move[1] - direction[1]][move[0] - direction[0]] = 0
                robot = (robot[0] + direction[0], robot[1] + direction[1])
    return robot


data = open('data/day_15.txt').read().splitlines()
n = data.index('')
char_map = {
    '#': -1,
    '.': 0,
    'O': 1,
    '@': 0,
    '[': 1,
    ']': 3
}
wide_map = {
    '#': '##',
    '.': '..',
    'O': '[]',
    '@': '@.'
}
dir_map = {
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0),
    '>': (1, 0)
}


def box_mover(wide=False):
    warehouse = []
    robot = (-1, -1)
    for idx in range(n):
        if '@' in data[idx]:
            robot = (data[idx].find('@'), idx) if not wide else (data[idx].find('@') * 2, idx)
        if wide:
            line = ''
            for char in data[idx]:
                line += wide_map[char]
            line = [char_map[char] for char in line]
        else:
            line = [char_map[char] for char in data[idx]]
        warehouse.append(line)

    for idx in range(n + 1, len(data)):
        for symbol in data[idx]:
            direction = dir_map[symbol]
            robot = move_boxes(direction, robot, warehouse, wide)

    sol = 0
    for y in range(len(warehouse)):
        for x in range(len(warehouse[0])):
            if warehouse[y][x] == 1:
                sol += y * 100 + x
    return sol


print(f'Part 1: {box_mover()}')
print(f'Part 2: {box_mover(True)}')
