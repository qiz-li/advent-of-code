# Find this puzzle at:
# https://adventofcode.com/2020/day/13

with open('input.txt', 'r') as file:
    puzzle_input = file.readlines()[1].split(',')
# This code works after discovering that given any amount of buses,
# the timestamps when all buses depart one by one a minute apart increases
# by a constant amount. E.g. the timestamp this happens for bus 7, 13 is at
# minute 77, the second time at minute 168, the third at minute 259,
# increasing with the constant difference of 91 (168 - 77).
# If we find this difference each time, the amount of numbers we
# will need to try to find our final answer will significantly decrease.
difference = int(puzzle_input[0])
initial = number = idx = 0
while idx < len(puzzle_input):
    number += difference
    if not initial:
        for bus in puzzle_input:
            # If bus id is 'x' we add one and keep on going
            if puzzle_input[idx] == 'x' or idx == 0:
                number += 1
                idx += 1
            elif puzzle_input[idx] != 'x':
                # We find the first timestamp and store it
                if number % int(puzzle_input[idx]) == 0:
                    if idx + 1 == len(puzzle_input):
                        print(number + 1 - len(puzzle_input))
                        idx += 1
                    initial = number
                break
    # Find the second timestamp and minus it with the first
    # to get the constant difference we need
    elif initial and number % int(puzzle_input[idx]) == 0:
        difference = number - initial
        number = initial - difference
        initial = 0
        number += 1
        idx += 1
