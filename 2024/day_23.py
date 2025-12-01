from collections import deque

data = open('data/day_23.txt').read().splitlines()


def graph_two_directions(data):
    graph = set()
    for line in data:
        a, b = line.split("-")
        graph.add((a, b))
        graph.add((b, a))
    return graph


def find_nearby_nodes(graph):
    nearby = {}
    for a, b in graph:
        if a not in nearby:
            nearby[a] = set()
        if b not in nearby:
            nearby[b] = set()
        nearby[a].add(b)
        nearby[b].add(a)
    return nearby


def find_triangles(nearby):
    found = set()
    sol = 0
    for a in nearby:
        for b in nearby[a]:
            for c in nearby[b]:
                if c in nearby[a] and a != b != c:
                    candidate = [a, b, c]
                    candidate = tuple(sorted(candidate))
                    if candidate in found:
                        continue
                    found.add(candidate)
                    if a[0] == 't' or b[0] == 't' or c[0] == 't':
                        sol += 1
    return sol

def find_cliques(nearby):
    largest = set()

    for a in nearby:
        queue = deque()
        clique = set([a])
        queue.append(a)

        while queue:
            node = queue.popleft()
            for neighbor in nearby[node]:
                if neighbor not in clique:
                    if all(neighbor in nearby[other] for other in clique):
                        queue.append(neighbor)
                        clique.add(neighbor)
        if len(largest) < len(clique):
            largest = clique

    return ','.join(sorted(largest))


graph = graph_two_directions(data)
nearby = find_nearby_nodes(graph)
print(find_triangles(nearby))

print(find_cliques(nearby))