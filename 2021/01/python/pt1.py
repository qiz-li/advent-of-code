import os
with open(f'{os.path.dirname(__file__)}/../input.txt', 'r') as file:
    puzzle_input = [int(i) for i in file.read().splitlines()]

count = 0
for idx, i in enumerate(puzzle_input):
    if idx != 0 and i > puzzle_input[idx - 1]:
        count += 1

print(count)
