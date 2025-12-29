from functools import cache
import numpy as np

with open("data/day_10.txt", "r") as f:
    data = f.read().splitlines()
data = [x.split(" ") for x in data]

goals = [x[0] for x in data]
goals = [list(map(lambda x: False if x=='.' else True, x.strip('[]'))) for x in goals]

joltages = [x[-1] for x in data]
joltages = [list(map(int,x.strip('{}').split(","))) for x in joltages]

buttons = [x[1:-1] for x in data]
buttons = [[tuple(map(int,x.strip('()').split(","))) for x in button_list] for button_list in buttons] 


####
# TOO SLOW
#######
# @cache
# def button_click(button, joltages):
#     result_joltages = list(joltages)
#     for light in button:
#         result_joltages[light] += 1
#     result = [False if x%2==0 else True for x in result_joltages]
#     return tuple(result), tuple(result_joltages)
# 
# part_1_result = 0
# part_2_result = 0
# for i in range(len(buttons)):
#     #current row
#     goal = tuple(goals[i])
#     joltage = tuple(joltages[i])
#     button_list = buttons[i]
#     
#     # initial value - (buttons, joltage)
#     solution = (tuple([False] * len(goal)),tuple([0] * len(goal)))
#     button_clicks = {solution[1]: 0}
#     button_clicks_short = {solution[0]: 0}
# 
#     part_1_goal = 99999999999
#     part_2_goal = 99999999999
#     
#     while part_1_goal == 99999999999 or part_2_goal == 99999999999:
#         new_button_clicks = {}
#         # for every possibility
#         for solution in button_clicks.keys():
#             # click every button
#             joltages_list = solution
#             for button in button_list:
#                 solution_candidate = tuple(button_click(button, joltages_list))
#                 # if the solution did not pass the joltage
#                 overjolt = False
#                 for idx, jolt in enumerate(solution_candidate[1]):
#                     if jolt > joltage[idx]:
#                         overjolt = True
#                 # add only if such a solution doesn't exist
#                 if not overjolt and solution_candidate[1] not in new_button_clicks.keys():
#                     new_button_clicks[solution_candidate[1]] = button_clicks[solution]+1
#                         
#                     # add for part 1
#                     button_clicks_short[solution_candidate[0]] = new_button_clicks[solution_candidate[1]]
#         button_clicks = new_button_clicks
# 
# 
#         if goal in button_clicks_short.keys():
#             part_1_goal = min(part_1_goal, button_clicks_short[goal])
#         if joltage in button_clicks.keys():
#             part_2_goal = min(part_2_goal, new_button_clicks[joltage])
#             
#     part_1_result +=  part_1_goal
#     part_2_result += part_2_goal
#     print("done")
# print(part_1_result, part_2_result)

for i in range(len(goals)):
    joltage_vector = np.array(joltages[i])
    buttons_array = [[1 if idx in button else 0 for idx in range(len(joltages[i]))] for button in buttons[i]]
    buttons_matrix = np.array(buttons_array)
    inverse = np.linalg.inv(buttons_matrix)
    x = np.dot(inverse, joltage_vector)