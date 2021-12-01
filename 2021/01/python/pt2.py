import os
with open(f'{os.path.dirname(__file__)}/../input.txt', 'r') as file:
    puzzle_input = [int(i) for i in file.read().splitlines()]

count = prev_sum = 0
for idx, i in enumerate(puzzle_input):
    if idx >= 2:
        sum = i + puzzle_input[idx - 1] + puzzle_input[idx - 2]
        if sum > prev_sum:
            count += 1
        prev_sum = sum

print(count-1)
