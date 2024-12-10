data = open("data/day_10.txt").read().splitlines()
data = [[int(cell) for cell in line] for line in data]


def traverse(grid, x, y, find_only_one=True):
    if find_only_one:
        paths = set()
    else:
        paths = []
    step(grid, x, y + 1, x, y, paths, find_only_one)
    step(grid, x, y - 1, x, y, paths, find_only_one)
    step(grid, x + 1, y, x, y, paths, find_only_one)
    step(grid, x - 1, y, x, y, paths, find_only_one)
    return len(paths)


def step(grid, x, y, prev_x, prev_y, sol, find_only_one):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[prev_y][prev_x] + 1 != grid[y][x]:
        return
    if grid[y][x] == 9:
        if find_only_one:
            sol.add((x, y))
        else:
            sol.append((x,y))
    step(grid, x, y + 1, x, y, sol, find_only_one)
    step(grid, x, y - 1, x, y, sol, find_only_one)
    step(grid, x + 1, y, x, y, sol, find_only_one)
    step(grid, x - 1, y, x, y, sol, find_only_one)
    return

sol = 0
sol2 = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == 0:
            sol += traverse(data, x, y)
            sol2 += traverse(data, x, y, False)
print(sol)
print(sol2)