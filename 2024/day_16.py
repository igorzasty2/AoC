import heapq

data = open('data/day_16.txt').read().splitlines()
start = (-1, -1)
end = (-1, -1)
symbol_map = {
    'S': False,
    'E': False,
    '#': True,
    '.': False
}
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

# Works for small mazes
def move(pos_x, pos_y, direction, points=0, tiles=None):
    if tiles is None:
        tiles = set()
    if (pos_x, pos_y) == end:
        return points
    if (pos_x, pos_y) in tiles or walls[pos_y][pos_x]:
        return -1
    tiles = tiles.copy()
    tiles.add((pos_x, pos_y))
    moves = [move(pos_x + directions[direction][0], pos_y + directions[direction][1], direction, points + 1, tiles),
             move(pos_x + directions[direction - 1][0], pos_y + directions[direction - 1][1], (direction - 1) % 4,
                  points + 1001, tiles),
             move(pos_x + directions[direction - 3][0], pos_y + directions[direction - 3][1], (direction - 3) % 4,
                  points + 1001, tiles)]
    valid = [x for x in moves if x != -1]
    return min(valid, default=-1)


def graph_maze():
    pq = []
    heapq.heappush(pq, (0, start[0], start[1], 0))
    visited = set()
    previous = {}
    sols = []
    while pq:
        cost, x, y, direction = heapq.heappop(pq)

        if (x, y) == end:
            sols.append(cost)
            continue

        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        for i in range(4):
            dx, dy = directions[i]
            if i == (direction - 2) % 4:
                continue
            nx, ny = x + dx, y + dy
            if not walls[ny][nx]:
                new_cost = cost + 1 if i == direction else cost + 1001
                if (nx, ny, new_cost) not in previous:
                    previous[(nx, ny, new_cost)] = []
                previous[(nx, ny, new_cost)].append((x, y, cost))
                heapq.heappush(pq, (new_cost, nx, ny, i))
    minimum_cost = min(sols)
    stack = [(end[0], end[1], minimum_cost)]

    tiles = set()
    while stack:
        x, y, cost = stack.pop()
        tiles.add((x, y))
        if (x, y, cost) in previous:
            for (prev_x, prev_y, prev_cost) in previous[(x, y, cost)]:
                if prev_cost == cost-1 or prev_cost == cost-1001:
                    stack.append((prev_x, prev_y, prev_cost))
    return minimum_cost, len(tiles)


walls = []
for col, line in enumerate(data):
    if line.find('E') != -1:
        end = (line.find('E'), col)
    elif line.find('S') != -1:
        start = (line.find('S'), col)
    walls.append([symbol_map[char] for char in line])

print('Solution:', graph_maze())
