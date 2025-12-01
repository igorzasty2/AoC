data = open("data/day_7.txt")


def check_equation(target, value, numbers):

    if len(numbers) == 0:
        return value == target

    else:
        return check_equation(target, value + numbers[0], numbers[1:]) or check_equation(target, value * numbers[0],
                                                                                         numbers[1:])


def check_equation_concat(target, value, numbers):
    if len(numbers) == 0:
        return value == target

    else:
        a = 10 ** len(str(numbers[0]))
        return (check_equation_concat(target, value + numbers[0], numbers[1:])
                or check_equation_concat(target, value * numbers[0], numbers[1:])
                or check_equation_concat(target, value * 10 ** len(str(numbers[0])) + numbers[0], numbers[1:]))


sol = 0
sol2 = 0
for line in data:
    eq, nums = line.strip().split(":")
    nums = list(map(int, nums.split()))
    eq = int(eq)
    if check_equation(eq, nums[0], nums[1:]):
        sol += eq
    if check_equation_concat(eq, nums[0], nums[1:]):
        sol2 += eq
print(sol)
print(sol2)
