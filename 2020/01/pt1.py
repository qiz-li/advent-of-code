# Find this puzzle at:
# https://adventofcode.com/2020/day/1

with open('input.txt', 'r') as file:
    puzzle_input = [int(i) for i in file.read().splitlines()]
# The numbers are 1010 + 1010
if puzzle_input.count(1010) == 2:
    print(1010**2)
else:
    for number in puzzle_input:
        # 2020 minus number is in the list
        if 2020 - number in puzzle_input:
            print(number * (2020-number))
            break
