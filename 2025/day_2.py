from math import ceil
data = open("data/day_2.txt").read().split("\n")[:-1]
data = data[0].split(",")

# Part 1
score = 0
for item in data:
    low, high = item.split("-")

    low_value = int(low)
    high_value = int(high)

    low_range = int(low[:ceil(len(low) // 2)] or 0)
    high_range = int(high[:ceil(len(high) / 2)])+1

    while low_range <= high_range:
        test_digit = int(str(low_range)*2)
        if low_value <= test_digit <= high_value:
            score+=test_digit
        low_range+=1

print(f"Part 1: {score}")

# Part 2
score_repeated = 0
found_numbers = set()
ranges = [list(map(int, x.split("-"))) for x in data]
all_numbers = set()
limit = max(ranges)[1]
limit_short = limit//pow(10,((len(str(limit)))//2))
i = 1
for range_group in ranges:
    all_numbers.update(range(range_group[0], range_group[1] + 1))
while i <= limit_short:
    curr_digit = str(i)
    test_num = curr_digit*2

    while int(test_num) < limit:
        if int(test_num) in all_numbers and not int(test_num) in found_numbers:
                print(test_num)
                score_repeated += int(test_num)
                found_numbers.add(int(test_num))
        test_num += curr_digit
    i+=1
print(f"Part 2: {score_repeated}")