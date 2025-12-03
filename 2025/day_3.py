data = open("data/day_3.txt").read().split("\n")[:-1]

# Part 1 - Legacy
# total_joltage = 0
#
# for line in data:
#     tens_digit = line[0]
#     ones_digit = "1"
#
#     idx = 1
#     while idx < len(line)-1:
#         digit = line[idx]
#         if digit > tens_digit:
#             ones_digit = "1"
#             tens_digit = digit
#         elif digit > ones_digit:
#             ones_digit = digit
#
#         idx += 1
#     if line[-1] > ones_digit:
#         ones_digit = line[-1]
#     total_joltage += int(tens_digit) * 10 + int(ones_digit)
#
# print("Part 1:", total_joltage)


# Part 1 & 2
def day_3(data, battery_length):
    total_joltage = 0
    for line in data:
        line = list(map(int, line))
        length = len(line)
        left_idx = -1
        right_buffer = -battery_length + 1

        line_joltage = 0
        while right_buffer <= 0:
            number = max(line[left_idx+1:length+right_buffer])
            left_idx = line.index(number, left_idx+1)
            right_buffer += 1
            line_joltage = line_joltage*10 + number
        total_joltage += line_joltage
    print(f"Total joltage for {battery_length} length battery:", total_joltage)

day_3(data, 2)
day_3(data, 12)