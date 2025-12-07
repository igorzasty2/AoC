data = open('data/day_6.txt', 'r').read().split('\n')[:-1]
data = [x.split() for x in data]

numbers = data[:-1]
ops = data[-1:][0]
total = 0
for idx, op in enumerate(ops):
    line_num = 0
    is_mult = op == '*'
    line_total = 1 if is_mult else 0
    while line_num < len(numbers):
        if is_mult:
            line_total *= int(numbers[line_num][idx])
        else:
            line_total += int(numbers[line_num][idx])
        line_num += 1
    total += line_total
print("Part 1: ",total)

data = open('data/day_6.txt', 'r').read().split('\n')[:-1]
numbers = data[:-1]
ops = data[-1:][0]
total_vertical = 0
idx = 0
while idx < len(ops):
    # Curr num length
    num_length = 1
    while idx+num_length < len(ops) and ops[idx+num_length] == ' ':
        num_length += 1
    if idx+num_length == len(ops):
        num_length += 1
    num_length -= 1
    # Get sign
    is_mult = ops[idx] == '*'
    line_total = 1 if is_mult else 0
    
    nums = [0]*num_length
    
    # For each row
    for line_num in range(len(numbers)):
        
        # For each digit in row
        for num in range(num_length):
            if numbers[line_num][idx+num] == ' ':
                continue
            nums[num]*=10
            nums[num]+=int(numbers[line_num][idx+num])

    #Finally make the equation
    for num in nums:
        if is_mult:
            line_total *= num
        else:
            line_total += num
    idx += num_length+1
    total_vertical += line_total
print("Part 2: ",total_vertical)