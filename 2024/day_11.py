data = open("data/day_11.txt").read().split()


def blink(stones: list, num_blinks: int) -> int:
    calcs = {}
    sol = 0
    for stone in stones:
        sol += mark_stone(stone, num_blinks, calcs)
    return sol


def mark_stone(stone: str, num_blinks: int, calcs: dict) -> int:
    if num_blinks == 0:
        return 1
    if stone in calcs and num_blinks in calcs[stone]:
        return calcs[stone][num_blinks]
    if stone == '0':
        res = mark_stone('1', num_blinks - 1, calcs)
    elif len(stone) % 2 == 0:
        res = mark_stone(stone[:len(stone) // 2], num_blinks - 1, calcs)
        res += mark_stone(str(int(stone[len(stone) // 2:])), num_blinks - 1, calcs)
    else:
        res = mark_stone(str(int(stone) * 2024), num_blinks - 1, calcs)
    if stone not in calcs:
        calcs[stone] = {}
    calcs[stone][num_blinks] = res
    return res


print(blink(data, 75))
