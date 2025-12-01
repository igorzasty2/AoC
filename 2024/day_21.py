from functools import cache
from itertools import permutations

data = open('data/day_21.txt').read().splitlines()


def map_array(grid):
    result = {}
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            result[char] = (row, col)
    return result


numpad = map_array(["789", "456", "123", "X0A"])
keypad = map_array(["X^A", "<v>"])


@cache
def is_valid_path(path, is_numpad, start):
    board = numpad if is_numpad else keypad
    death_square = board["X"]
    y, x = board[start]
    moves = {
        "<": (0, -1),
        ">": (0, 1),
        "^": (-1, 0),
        "v": (1, 0)
    }
    for move in path:
        dy, dx = moves[move]
        y, x = y + dy, x + dx
        if x == 0 and y == death_square[0]:
            return False
    return True


@cache
def find_paths(is_numpad, start, end):
    board = numpad if is_numpad else keypad

    start_y, start_x = board[start]
    end_y, end_x = board[end]

    horizontal = '<' * max(0, start_x - end_x) + '>' * max(0, end_x - start_x)
    vertical = '^' * max(0, start_y - end_y) + 'v' * max(0, end_y - start_y)
    result = horizontal + vertical
    paths = []
    for perm in set(permutations(result)):
        perm = "".join(perm)
        if is_valid_path(perm, is_numpad, start):
            paths.append(perm + "A")
    return paths


@cache
def decode(res, loops, is_numpad=True):
    state = 'A'
    sol = 0
    for input_commands in res:
        paths = find_paths(is_numpad, state, input_commands)
        if loops == 0:
            sol += min(len(path) for path in paths)
        else:
            sol += min(decode(path, loops - 1, False) for path in paths)
        state = input_commands
    return sol


def remote_control(degrees_of_idiocy, input_commands_list):
    if degrees_of_idiocy < 0:
        print("Not stupid enough")
        return 0
    sol = 0
    for input_commands in input_commands_list:
        length = decode(input_commands, degrees_of_idiocy)
        number = int(input_commands[:-1])
        sol += length * number
    return sol


print(remote_control(2, data))
print(remote_control(25, data))
