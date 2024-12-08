data = open("data/day_8.txt").read().splitlines()


def in_bounds(x, y):
    return False if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data) else True


symbols = {}

for idy, line in enumerate(data):
    for idx, symbol in enumerate(line):
        if symbol != ".":
            if symbol not in symbols:
                symbols[symbol] = [(idx, idy)]
            else:
                symbols[symbol].append((idx, idy))

antinodes = set()
for symbol, values in symbols.items():
    n = len(values)
    for i in range(n):
        pos1_x, pos1_y = values[i]
        for j in range(i + 1, n):
            pos2_x, pos2_y = values[j]
            vector = [pos2_x - pos1_x, pos2_y - pos1_y]  # 2+ 1-
            if in_bounds(pos2_x + vector[0], pos2_y + vector[1]):
                antinodes.add((pos2_x + vector[0], pos2_y + vector[1]))
            if in_bounds(pos1_x - vector[0], pos1_y - vector[1]):
                antinodes.add((pos1_x - vector[0], pos1_y - vector[1]))
print(len(antinodes))

antinodes = set()
for symbol, values in symbols.items():
    n = len(values)
    for i in range(n):
        pos1_x, pos1_y = values[i]
        for j in range(i + 1, n):
            pos2_x, pos2_y = values[j]
            vector = [pos2_x - pos1_x, pos2_y - pos1_y]  # 2+ 1-
            new_pos1 = pos1_x, pos1_y
            new_pos2 = pos2_x, pos2_y
            while in_bounds(new_pos2[0], new_pos2[1]):
                antinodes.add(new_pos2)
                new_pos2 = (new_pos2[0] + vector[0], new_pos2[1] + vector[1])
            while in_bounds(new_pos1[0], new_pos1[1]):
                antinodes.add(new_pos1)
                new_pos1 = (new_pos1[0] - vector[0], new_pos1[1] - vector[1])
print(len(antinodes))
