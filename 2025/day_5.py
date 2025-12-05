data = open('data/day_5.txt', 'r').read().split('\n')[:-1]

ranges = data[:data.index('')]
values = data[data.index('')+1:]

values = list(map(int, values))
food_lists = []
for i in ranges:
    tup = tuple(map(int, i.split('-')))
    food_lists.append(tup)

def can_join_ranges(range_1, range_2):
    if range_1[0] <= range_2[0] <= range_1[1] or range_2[0] <= range_1[0] <= range_2[1]:
        return True
    else:
        return False

left_idx = 0
while left_idx < len(food_lists)-1:
    right_idx = left_idx + 1
    while right_idx < len(food_lists):
        curr_food_list = food_lists[left_idx]
        next_food_list = food_lists[right_idx]
        if can_join_ranges(curr_food_list, next_food_list):
            tmp = (min(curr_food_list[0], next_food_list[0]), max(curr_food_list[1], next_food_list[1]))
            food_lists.remove(curr_food_list)
            food_lists.remove(next_food_list)
            food_lists.append(tmp)
            left_idx-=1
            break
        right_idx += 1
    left_idx += 1

# Part 1
fresh = 0
for value in values:
    for food_list in food_lists:
        if food_list[0] <= value <= food_list[1]:
            fresh += 1
            break

# Part 2
fresh_ids = 0
for food_list in food_lists:
    fresh_ids += food_list[1] - food_list[0] + 1


print("Part 1: ", fresh)
print("Part 2: ", fresh_ids)