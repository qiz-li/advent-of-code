# Find this puzzle at:
# https://adventofcode.com/2020/day/15

with open('input.txt', 'r') as file:
    puzzle_input = [int(i) for i in file.read().split(',')]
original_len = len(puzzle_input)
for idx in range(2020 - len(puzzle_input)):
    idx += original_len
    last = puzzle_input[idx - 1]
    # If it is the first time the number has been spoken, add zero.
    if last not in puzzle_input:
        puzzle_input.append(0)
    else:
        # Else find how many turns are between the two most recent occurrences
        try:
            last_spoken = (len(puzzle_input) - 1 - puzzle_input
                           [idx - 2::-1].index(last))
            turns_aprt = idx - last_spoken
            puzzle_input.append(turns_aprt)
        # If this is the first time spoken after the starting number, add zero.
        except ValueError:
            puzzle_input.append(0)
print(puzzle_input[-1])
