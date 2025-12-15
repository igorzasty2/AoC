from collections import Counter

with open("data/day_9.txt", "r") as f:
    data = f.read().splitlines()
data = [tuple(map(int, x.split(","))) for x in data]

areas = dict()
for i in range(len(data)):
    tile_1 = data[i]
    for j in range(i + 1, len(data)):
        tile_2 = data[j]
        area = (abs(tile_2[0] - tile_1[0]) + 1) * (abs(tile_2[1] - tile_1[1]) + 1)
        areas[area] = (i, j)
        
max_area = max(areas.keys())
print(max_area)
max_tiles = areas[max_area]
print(max_tiles)
data.append(data[0])
for area in sorted(areas.keys(), reverse=True):
    edge_1, edge_2 = areas[area]
    x_bound = sorted((data[edge_1][0], data[edge_2][0]))
    y_bound = sorted((data[edge_1][1], data[edge_2][1]))
    valid = True
    for tile_idx in range(len(data)-1):
        tile_1, tile_2 = data[tile_idx], data[tile_idx+1]
        is_vertical = tile_1[0] == tile_2[0]
        
        if is_vertical:
            # X nie w zasięgu
            if not(x_bound[0] < tile_1[0] < x_bound[1]):
                continue
                
            tile_1, tile_2 = sorted((tile_1[1], tile_2[1]))
            if tile_1 < y_bound[1] and tile_2 > y_bound[0]:
                valid = False
                break
        else:
            if not(y_bound[0] < tile_1[1] < y_bound[1]):
                continue
            
            tile_1, tile_2 = sorted((tile_1[0], tile_2[0]))
            if tile_1 < x_bound[1] and tile_2 > x_bound[0]:
                valid = False
                break
    if valid:
        print(area)
        break