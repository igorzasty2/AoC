input_data = open("data/day_9.txt").read()


def part_one(data):
    block = []
    file_id = 0
    for idx, cell in enumerate(data):
        if idx % 2 == 0:
            block.extend([file_id] * int(cell))
            file_id += 1
        else:
            block.extend([-1] * int(cell))

    left_pointer = 0
    right_pointer = len(block) - 1
    while left_pointer < right_pointer:
        if block[left_pointer] != -1:
            left_pointer += 1
            continue
        if block[right_pointer] == -1:
            right_pointer -= 1
            continue
        block[left_pointer], block[right_pointer] = block[right_pointer], block[left_pointer]
        left_pointer += 1
        right_pointer -= 1
    return sum(cell * idx if cell != -1 else 0 for idx, cell in enumerate(block))


def part_two(data):
    blocks = []
    file_id = 0
    for idx, cell in enumerate(data):
        if idx % 2 == 0:
            blocks.append([file_id, int(cell)])
            file_id += 1
        else:
            blocks.append([-2, int(cell)])

    idx = 0
    while idx < len(blocks):
        block = blocks[idx]
        if block[0] == -2:
            for i in reversed(range(idx, len(blocks))):
                fit_block = blocks[i]
                if fit_block[0] >= 0 and block[1] >= fit_block[1]:
                    block[1] -= fit_block[1]
                    blocks.insert(idx, fit_block)
                    idx += 1

                    blocks.reverse()
                    blocks[blocks.index(fit_block)] = [-1, fit_block[1]]
                    blocks.reverse()
        idx += 1
    sol = 0
    idx = 0
    for block in blocks:
        for i in range(block[1]):
            sol += block[0] * idx if block[0] >= 0 else 0
            idx += 1
    return sol


print(part_one(input_data))
print(part_two(input_data))
