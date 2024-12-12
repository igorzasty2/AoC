from collections import deque

data = open("data/day_12.txt").read().splitlines()


def in_bounds(row, col, data):
    return False if col < 0 or row < 0 or col >= len(data[0]) or row >= len(data) else True


def fence_price(data, is_bulk_discount=False):
    visited = [[False] * len(data[0]) for _ in range(len(data))]
    queue = deque()
    sol = 0

    for y in range(len(data)):
        for x in range(len(data[0])):
            if not visited[y][x]:
                target = data[y][x]
                queue.append((y, x, None))
                area = 0
                walls = set()

                while queue:
                    check_y, check_x, direction = queue.popleft()
                    if in_bounds(check_y, check_x, data) and data[check_y][check_x] == target:
                        if not visited[check_y][check_x]:
                            visited[check_y][check_x] = True
                            area += 1
                            queue.append((check_y + 1, check_x, 0))
                            queue.append((check_y - 1, check_x, 2))
                            queue.append((check_y, check_x + 1, 1))
                            queue.append((check_y, check_x - 1, 3))
                    else:
                        walls.add((check_y, check_x, direction))
                if is_bulk_discount:
                    walls = list(walls)
                    long_walls = set()  # y x is_vertical
                    walls.sort()
                    for wall in walls:
                        wall_y, wall_x, direction = wall
                        # Up down
                        if direction % 2 == 0:
                            long_wall = next((w for w in long_walls if (wall_y, wall_x - 1, direction) == w), None)
                            if long_wall:
                                long_walls.remove(long_wall)
                            long_walls.add(wall)

                        # Left Right
                        else:
                            long_wall = next((w for w in long_walls if (wall_y - 1, wall_x, direction) == w), None)
                            if long_wall:
                                long_walls.remove(long_wall)
                            long_walls.add(wall)

                sol += len(long_walls) * area if is_bulk_discount else len(walls) * area
    return sol


print("Part 1: {}".format(fence_price(data)))
print("Part 2: {}".format(fence_price(data, True)))
