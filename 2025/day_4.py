from helpers import in_bounds
data = open("data/day_4.txt").read().split("\n")[:-1]
data = [list(x) for x in data]

def remove_rolls(boxes):
    neighbours = [[0] * len(boxes[0]) for i in range(len(boxes))]
    for y, line in enumerate(boxes):
        for x, symbol in enumerate(line):
            if symbol != "@":
                continue
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if in_bounds(j + x, i + y, boxes):
                        neighbours[y + i][x + j] += 1
    blocks = 0
    for y in range(len(boxes)):
        for x in range(len(boxes[0])):
            current = neighbours[y][x]
            if neighbours[y][x] < 4 and boxes[y][x] == "@":
                blocks += 1
                boxes[y][x] = "."
    return blocks


def remove_recursion(box_state):
    score = -1
    new_score = 0
    while score != new_score:
        score = new_score
        new_score += remove_rolls(box_state)
    return new_score


# Part 1
print(remove_rolls(data))

data = open("data/day_4.txt").read().split("\n")[:-1]
data = [list(x) for x in data]

# Part 2
print(remove_recursion(data))