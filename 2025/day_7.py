data = open('data/day_7.txt').read().splitlines()
beams = [[0]*len(data[0]) for _ in range(len(data))]
start_beam = data[0].find('S')
splits = 0
beams[0][start_beam] = 1
for idx, line in enumerate(data[1:], 1):
    for idx_char, char in enumerate(line):
        if beams[idx-1][idx_char]>0:
            if char == '^':
                splits += 1
                beams[idx][idx_char-1] += beams[idx-1][idx_char]
                beams[idx][idx_char+1] += beams[idx-1][idx_char]
            else:
                beams[idx][idx_char] += beams[idx-1][idx_char]
print("Part 1: ", splits)
print("Part 2: ", sum(beams[-1]))