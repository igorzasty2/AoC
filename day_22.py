from collections import deque, Counter
from functools import cache

data = open('data/day_22.txt').read().splitlines()


@cache
def pseudorandom(secret):
    secret_a = secret << 6
    secret = secret ^ secret_a
    secret = secret % 16777216

    secret_a = secret >> 5
    secret = secret ^ secret_a
    secret = secret % 16777216

    secret_a = secret << 11
    secret = secret ^ secret_a
    secret = secret % 16777216
    return secret


def part_1():
    s = 0
    for value in data:
        value = int(value)
        for _ in range(2000):
            value = pseudorandom(value)
        s += value
    return s


def part_2():
    all_trades = Counter()
    for value in data:
        trades = Counter()
        value = pseudorandom(int(value))
        diffs = deque(maxlen=4)
        for _ in range(1999):
            prev = value
            value = pseudorandom(prev)
            diffs.append(value % 10 - prev % 10)
            if len(diffs) == 4:
                if tuple(diffs) not in trades:
                    trades[tuple(diffs)] = value % 10
        all_trades.update(trades)
    return max(all_trades.values())


print(part_1())
print(part_2())
