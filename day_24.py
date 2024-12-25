from collections import deque

data = open('data/day_24.txt').read().splitlines()
n = data.index("")
prev = {}

def solve():
    wires = {}
    for i in range(n):
        key, value = data[i].split(": ")
        wires[key] = int(value)
        prev[key] = value
    queue = deque()
    for i in range(n + 1, len(data)):
        val1, op, val2, _, out = data[i].split(" ")
        queue.append((val1, op, val2, out))

    while queue:
        val1, op, val2, out = queue.popleft()
        if val1 not in wires or val2 not in wires:
            queue.append((val1, op, val2, out))
            continue
        match op:
            case "AND":
                wires[out] = wires[val1] & wires[val2]
                op = "&"
            case "OR":
                wires[out] = wires[val1] | wires[val2]
                op = "|"
            case "XOR":
                wires[out] = wires[val1] ^ wires[val2]
                op = "^"
        prev[out] = (val1+op+val2)
    return "".join(
        str(entry[1]) for entry in sorted(filter(lambda e: e[0].startswith("z"), wires.items()), reverse=True))


print(int(solve(), 2))

