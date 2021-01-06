# Find this puzzle at:
# https://adventofcode.com/2020/day/1

with open('input.txt', 'r') as file:
    puzzle_input = [int(i) for i in file.read().splitlines()]
for number in puzzle_input:
    for number2 in puzzle_input:
        # 2020 minus any two entries is in the list
        if 2020 - number - number2 in puzzle_input:
            # Continue if one entry is being used twice
            if (len([number, number2, 2020 - number - number2]) !=
               len(set([number, number2, 2020 - number - number2])) and
               puzzle_input.count(number) + puzzle_input.count(number2) == 2):
                continue
            # Else we've found the answer
            else:
                print(number * number2 * (2020 - number - number2))
                break
    else:
        continue
    break
