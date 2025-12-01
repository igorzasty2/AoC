data = open("data/day_1.txt").read().split("\n")[:-1]
# licznik od 0 do 99, jeśli przekręcisz na 100 to wraca się do 0
# part 1, ile razy kończy na zerze
# part 2, ile razy przechodzi przez zero


# Part 1
safe_num = 50
zeroes = 0
for row in data:
    dir = 1 if row[0] == "R" else -1
    move_size = int(row[1:])
    safe_num = (safe_num + move_size * dir) % 100
    if safe_num == 0:
        zeroes += 1
print(f"Part 1: {zeroes}")


# Part 2
safe_num = 50
free_pass = False
zero_crosses = 0


for row in data:
    dir = 1 if row[0] == "R" else -1
    move_size = int(row[1:])

    zero_crosses = zero_crosses + move_size // 100
    move_size = move_size % 100
    safe_num = (safe_num + move_size * dir)

    if safe_num <= 0 or safe_num >= 100:
        if safe_num+move_size==0:
            pass
        else:
            zero_crosses += 1
        safe_num = safe_num % 100

print(f"Part 2: {zero_crosses}")