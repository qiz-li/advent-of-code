# Find this puzzle at:
# https://adventofcode.com/2020/day/10

with open('input.txt', 'r') as file:
    puzzle_input = [int(i) for i in file.read().splitlines()]
# Add the charging outlet (0) and the built-in joltage adapter (max + 3)
puzzle_input += [0] + [max(puzzle_input) + 3]
puzzle_input.sort()
one_jolt = three_jolts = 0
# For each adapter, check the next one to see
# whether it is either one jolt or three jolts.
for idx, adapter in enumerate(puzzle_input):
    if idx + 1 == len(puzzle_input):
        break
    elif puzzle_input[idx + 1] == adapter + 1:
        one_jolt += 1
    elif puzzle_input[idx + 1] == adapter + 3:
        three_jolts += 1
print(one_jolt * three_jolts)
