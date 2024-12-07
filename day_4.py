data = open("data/day_4.txt").read().splitlines()

def check_dir(data: list[str], x: int, y: int, word: str, dir_x: int, dir_y: int) -> bool:
    if word == "":
        return True
    if not (0 <= x + dir_x <= len(data[0]) - 1 and 0 <= y + dir_y <= len(data) - 1):
        return False
    if word[0] == data[y + dir_y][x + dir_x]:
        return check_dir(data, x + dir_x, y + dir_y, word[1:], dir_x, dir_y)
    else:
        return False


# Part 1

val = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "X":
            for x_dir in range(-1, 2):
                for y_dir in range(-1, 2):
                    val = val + 1 if check_dir(data, x, y, "MAS", x_dir, y_dir) else val
print(val)


# Part 2

val = 0
for y in range(1, len(data) - 1):
    for x in range(1, len(data[0]) - 1):
        if data[y][x] == "A":
            cross = 0
            for x_dir in [-1, 1]:
                for y_dir in [-1, 1]:
                    if data[y + y_dir][x + x_dir] == "M" and data[y - y_dir][x - x_dir] == "S":
                        cross += 1
            val += 1 if cross == 2 else 0
print(val)
