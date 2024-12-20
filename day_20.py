from collections import deque

data = open('data/day_20.txt').read().splitlines()
n = (len(data[0]), len(data))
start = (-1, -1)
end = (-1, -1)
path = set()
for j, line in enumerate(data):
    for i, letter in enumerate(line):
        if letter == "S":
            start = (i, j)
            path.add((i, j))
        elif letter == "E":
            end = (i, j)
            path.add((i, j))
        elif letter == ".":
            path.add((i, j))


def bfs():
    queue = deque()
    visited = {}
    queue.append((start[0], start[1], 0))
    while queue:
        x, y, dist = queue.popleft()
        if (x, y) not in path or (x, y) in visited:
            continue
        visited[(x, y)] = dist
        if (x, y) == end:
            return visited
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            queue.append((nx, ny, dist + 1))


def in_bounds(x, y):
    return 0 <= x <= n[0] and 0 <= y <= n[1]


def cheat(move_list, target_skip=100, max_skip=20):
    cheats = []
    for move in path:
        dist = move_list[move]
        for dy in range(-max_skip, max_skip + 1):
            for dx in range(-max_skip + abs(dy), max_skip + 1 - abs(dy)):
                nx, ny = move[0] + dx, move[1] + dy

                if in_bounds(nx, ny) and (nx, ny) in move_list:
                    skip_amount = move_list[(nx, ny)] - (dist + abs(dy) + abs(dx))

                    if skip_amount >= target_skip:
                        cheats.append(skip_amount)
    return cheats


road = bfs()
sol = cheat(road, target_skip=100, max_skip=2)
print(len(sol))

sol = cheat(road, target_skip=100, max_skip=20)
print(len(sol))
