data = open('data/day_2.txt')


# Part 1
def isCorrect(line):
    mod = 1 if line[-1] - line[0] > 0 else -1
    for i in range(1, len(line)):
        if not (0 < (line[i] - line[i - 1]) * mod < 4):
            return False
    return True


sol = sol2 = 0
for line in data:
    line = list(map(int, line.split()))
    sol += 1 if isCorrect(line) else 0

    # Part 2
    for n in range(len(line)):
        line_copy = list(line)
        del line_copy[n]
        if isCorrect(line_copy):
            sol2 += 1
            break

print(f"0 mistakes: {sol}")
print(f"1 mistake: {sol2}")
