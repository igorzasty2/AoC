import re
# data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
data = open('data/day_3.txt').read()
# split_data = data.split('mul(')
# sol = 0
# for i in range(len(split_data)):
#     end = split_data[i].find(')')
#     if end == -1:
#         continue
#     val = split_data[i][:end]
#     val = val.split(',')
#     mul = 1
#     for j in val:
#         if j.isnumeric():
#             mul *= int(j)
#         else:
#             mul = 0
#     sol += mul
# print(sol)


# Part 1
def count_mults(text: str) -> int:
    mults = r'mul\([0-9]+,[0-9]+\)'
    numbers = r'[0-9]+'
    matches = re.findall(mults, text)
    sol = 0
    for match in matches:
        number_pairs = re.findall(numbers, match)
        product = int(number_pairs[0]) * int(number_pairs[1])
        sol += product
    return sol

print(count_mults(data))

# Part 2
dont_regex = r"(?<=do\(\))(.*?)(?=don't\(\))"
new_data = re.findall(dont_regex, "do()" + data + "don't()", flags=re.DOTALL)
new_data = "".join(new_data)

print(count_mults(new_data))
