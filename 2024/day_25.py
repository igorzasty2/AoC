data = open('data/day_25.txt').read().splitlines()
data.append("")
keys = set()
locks = set()
box = []


def count_box(grid):
    lengths = [-1, -1, -1, -1, -1]
    for i in range(7):
        for j in range(5):
            if grid[i][j] == '#':
                lengths[j] += 1

    return tuple(lengths)


for line in data:
    if line == "":
        sol = count_box(box)
        if box[0][0] == ".":
            keys.add(sol)
        else:
            locks.add(sol)
        box = []
        continue
    box.append(line)

sol = 0
for key in keys:
    for lock in locks:
        if all(a + b <= 5 for a, b in zip(key, lock)):
            sol += 1
print(sol)
