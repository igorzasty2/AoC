data = open('data/day_19.txt').read().splitlines()
towels = set(data[0].split(", "))
checked = {"": 1}


def match(complex_towel):
    if complex_towel in checked:
        return checked[complex_towel]
    score = 0
    found = False
    for i in range(len(complex_towel)):
        towel_part = complex_towel[:i + 1]
        towel_complement = complex_towel[i + 1:]

        if towel_part in towels:
            temp_score = match(towel_complement)
            score = score + temp_score
            if temp_score > 0:
                if complex_towel in checked:
                    checked[complex_towel] += temp_score
                else:
                    checked[complex_towel] = temp_score
                found = True

    if not found:
        checked[complex_towel] = 0

    return score


sols = []
vibes = []
for line in data[2:]:
    sols.append(match(line))
    vibes.append(checked[line])
print(len([s for s in sols if s>0]))
print(sum(vibes))
