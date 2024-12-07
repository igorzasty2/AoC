data = open("data/day_5.txt").read().splitlines()
i = 0
sol = 0
orderdict = {}
while data[i] != '':
    left, right = data[i].split("|")
    if left in orderdict:
        orderdict[left].append(right)
    else:
        orderdict[left] = [right]
    i += 1
i += 1
pointer = i
# Part 1
while i < len(data):
    cells = data[i].split(",")
    correct = True
    for j in range(len(cells)):
        for k in range(j):
            if cells[j] in orderdict and cells[k] in orderdict[cells[j]]:
                correct = False
    if correct:
        sol += int(cells[len(cells) // 2])
    i += 1
print(f"Correct: {sol}")

sol2 = 0
i = pointer
while i < len(data):
    cells = data[i].split(",")
    correct = False
    while not correct:
        correct = True
        for j in range(len(cells)):
            for k in range(j):
                if cells[j] in orderdict and cells[k] in orderdict[cells[j]]:
                    correct = False
                    cells[j], cells[k] = cells[k], cells[j]
                    break
            if not correct:
                break
    sol2 += int(cells[len(cells) // 2])
    i += 1
print(f"Fixed: {sol2 - sol}")
