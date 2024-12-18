from collections import deque

data = open('data/day_18.txt').read().splitlines()

load_size = 1024
mem_size = 70

walls = set()
for i in range(load_size):
    a = tuple(map(int, data[i].split(',')))
    walls.add(a)


def in_bounds(x, y):
    return 0 <= x <= mem_size and 0 <= y <= mem_size


def traverse():
    visited = set()
    queue = deque()
    queue.append((0, 0, 0))
    while queue:
        x, y, steps = queue.popleft()
        if not in_bounds(x, y) or (x, y) in walls or (x, y) in visited:
            continue
        if x == mem_size and y == mem_size:
            return steps
        visited.add((x, y))
        queue.append((x + 1, y, steps+1))
        queue.append((x - 1, y, steps+1))
        queue.append((x, y + 1, steps+1))
        queue.append((x, y - 1, steps+1))

print(traverse())
for i in range(load_size, len(data)):
    a = tuple(map(int, data[i].split(',')))
    walls.add(a)
    if traverse() is None:
        print(a)
        break
