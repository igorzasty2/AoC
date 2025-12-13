with open("data/day_8.txt", 'r', encoding='utf-8') as f:
    data = f.read().splitlines()
data = [list(map(int, x.split(","))) for x in data]
dist_reverse = dict()
furthers = []
for idx in range(len(data)):
    edge = data[idx]
    for jdx in range(idx + 1, len(data)):
        neighbor = data[jdx]
        delta_x = pow(neighbor[0] - edge[0], 2)
        delta_y = pow(neighbor[1] - edge[1], 2)
        delta_z = pow(neighbor[2] - edge[2], 2)
        edge_dist = delta_x + delta_y + delta_z
        dist_reverse[edge_dist] = (idx, jdx)

# Part 1
circuits = []
CONNECTIONS_TO_FIND = 10
while CONNECTIONS_TO_FIND > 0:
    curr_min = min(dist_reverse.keys())
    next_candidate = dist_reverse[curr_min]
    dist_reverse.pop(curr_min)
    found_idx = -1
    found_circuit = False
    circuit_break = False
    for idx, circuit in enumerate(circuits):
        if next_candidate[0] in circuit or next_candidate[1] in circuit:
            if next_candidate[0] in circuit and next_candidate[1] in circuit:
                circuit_break = True
                break
            found_circuit = True
            found_idx = idx
            
            circuit.append(next_candidate[1]) if next_candidate[0] in circuit else circuit.append(next_candidate[0])
            for jdx, other_circuit in enumerate(circuits):
                if idx == jdx:
                    continue
                if next_candidate[0] in other_circuit or next_candidate[1] in other_circuit:
                    circuit.remove(next_candidate[1]) if next_candidate[1] in other_circuit else circuit.remove(next_candidate[0])
                    circuit.extend(other_circuit)
                    circuits.remove(other_circuit)
    if not found_circuit and not circuit_break:
        circuits.append([next_candidate[0], next_candidate[1]])
    CONNECTIONS_TO_FIND = CONNECTIONS_TO_FIND - 1

print(circuits)
circuit_len = list(map(len, circuits))
top_three = sorted(circuit_len, reverse=True)[:3]
print(top_three[0]*top_three[1]*top_three[2])

# Part 2
while len(circuits[0]) != len(data):
    curr_min = min(dist_reverse.keys())
    next_candidate = dist_reverse[curr_min]
    dist_reverse.pop(curr_min)
    found_idx = -1
    found_circuit = False
    circuit_break = False
    for idx, circuit in enumerate(circuits):
        if next_candidate[0] in circuit or next_candidate[1] in circuit:
            if next_candidate[0] in circuit and next_candidate[1] in circuit:
                circuit_break = True
                break
            found_circuit = True
            found_idx = idx

            circuit.append(next_candidate[1]) if next_candidate[0] in circuit else circuit.append(next_candidate[0])
            for jdx, other_circuit in enumerate(circuits):
                if idx == jdx:
                    continue
                if next_candidate[0] in other_circuit or next_candidate[1] in other_circuit:
                    circuit.remove(next_candidate[1]) if next_candidate[1] in other_circuit else circuit.remove(
                        next_candidate[0])
                    circuit.extend(other_circuit)
                    circuits.remove(other_circuit)
    if not found_circuit and not circuit_break:
        circuits.append([next_candidate[0], next_candidate[1]])
print(next_candidate)
print(data[next_candidate[0]])
print(data[next_candidate[1]])
print(data[next_candidate[0]][0]*data[next_candidate[1]][0])