import re

data = open("data/day_13.txt").read()
nums = re.findall(r'\d+', data)
nums = list(map(int, nums))


def find_prize(a_1, a_2, b_1, b_2, p_1, p_2):
    det = a_1 * b_2 - a_2 * b_1
    if det == 0:
        print("No prize found")
    else:
        det_a = (p_1 * b_2 - p_2 * b_1)
        det_b = (a_1 * p_2 - a_2 * p_1)
        if det_a % det == 0 and det_b % det == 0:
            a = det_a // det
            b = det_b // det
            return 3 * a + b
    return 0

def clean_resort(nums, error=False):
    i = 0
    sol = 0
    while i < len(nums) - 1:
        if not error:
            sol += find_prize(nums[i], nums[i + 1], nums[i + 2], nums[i + 3], nums[i + 4], nums[i + 5])
        else:
            sol += find_prize(nums[i], nums[i + 1], nums[i + 2], nums[i + 3],
                              nums[i + 4] + 10000000000000, nums[i + 5] + 10000000000000)
        i += 6
    return sol


print("Part 1: {0}".format(clean_resort(nums)))
print("Part 2: {0}".format(clean_resort(nums, True)))
