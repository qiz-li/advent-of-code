# Find this puzzle at:
# https://adventofcode.com/2020/day/9

with open('input.txt', 'r') as file:
    puzzle_input = [int(i) for i in file.read().splitlines()]
for idx in range(len(puzzle_input)):
    numbers_sum = 0
    numbers_lst = []
    # Try each number in the list.
    # No need to keep on adding if the sum is already above our number.
    while numbers_sum <= 167829540:
        # The value of the first number and
        # each number after the first is added to the "numbers_sum"
        numbers_sum += puzzle_input[idx]
        numbers_lst.append(puzzle_input[idx])
        idx += 1
        # If "numbers_sum" adds up to our number,
        # we have found our list of numbers!
        if numbers_sum == 167829540 and len(numbers_lst) != 1:
            print(min(numbers_lst) + max(numbers_lst))
            break
    else:
        continue
    break
