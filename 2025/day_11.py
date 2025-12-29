from collections import deque

with open('data/day_11.txt') as f:
    data = f.readlines()

devices = dict()

for row in data:
    device, connections = row.split(':')
    devices[device] = connections.strip().split(' ')
    
def part1(target):
    queue = deque()
    queue_val = deque()
    sol = 0
    queue.append(target)
    queue_val.append(1)
    while queue:
        device = queue.popleft()
        value = queue_val.popleft()
        if device == "out":
            sol += value
            continue
        for output in devices[device]:
            if output in queue:
                queue_val[queue.index(output)] += value
            else:
                queue.append(output)
                queue_val.append(value)
    return sol


def part2(target):
    queue = deque()
    queue_val = deque()
    sol = 0
    queue.append((target,False,False))
    queue_val.append(1)
    while queue:
        device = queue.popleft() # "aaa", fal, fal
        value = queue_val.popleft() # 1
        if device[0] == "out":
            if device[1] is True and device[2] is True:
                sol += value
            continue
        for output in devices[device[0]]:
            candidate = (output,True if output == "fft" else device[1],True if output == "dac" else device[2])
            if candidate in queue:
                queue_val[queue.index(candidate)] += value
            else:
                queue.append(candidate)
                queue_val.append(value)
    return sol

print(part1("you"))
print(part2("svr"))