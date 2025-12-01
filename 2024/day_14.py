from PIL import Image, ImageDraw, ImageFont

data = open('data/day_14.txt').read().splitlines()
positions = []
velocities = []
for line in data:
    p, v = line.split(' v=')
    p = list(map(int, p[2:].split(',')))
    v = list(map(int, v.split(',')))
    positions.append(p)
    velocities.append(v)


def security_factor(positions, velocities, seconds):
    x_bound = 101
    y_bound = 103
    count = [0, 0, 0, 0]  # UL, UR, DL, DR
    blocks = set()
    for i in range(len(positions)):
        p = positions[i]
        v = velocities[i]
        p[0] = (p[0] + seconds * v[0]) % x_bound
        p[1] = (p[1] + seconds * v[1]) % y_bound
        check = 0
        blocks.add((p[0], p[1]))
        if p[0] == x_bound // 2 or p[1] == y_bound // 2:
            continue
        if p[0] > x_bound // 2:
            check += 1
        if p[1] > y_bound // 2:
            check += 2
        count[check] += 1
    sol = 1
    for i in count:
        sol *= i
    return sol, blocks


def print_robots(positions, nr):
    image = Image.new('1', (103, 101), 1)
    pixels = image.load()
    for i in range(101):
        for j in range(103):
            if (j, i) in positions:
                pixels[j, i] = 0
            else:
                pixels[j, i] = 1
        image.save('temp/' + str(nr) + '.png')
    return


print(security_factor(positions, velocities, 100)[0])
reps = 100
for _ in range(10000):
    _, blocks = security_factor(positions, velocities, 1)
    reps += 1
    print_robots(blocks, reps)
