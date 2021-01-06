# Find this puzzle at:
# https://adventofcode.com/2020/day/12

with open('input.txt', 'r') as file:
    puzzle_input = file.read().splitlines()
directions = ['N', 'E', 'S', 'W']
currently = 'E'
idx = 1
ew = ns = 0
for instruc in puzzle_input:
    # Seperate the action and the value
    action = ''.join([i for i in instruc if not i.isdigit()])
    value = int(''.join([i for i in instruc if i.isdigit()]))
    # Turn to the specified direction
    if action in ('R', 'L'):
        turn = value//90
        if action == 'L':
            turn = 4 - turn
        idx += turn
        if idx >= len(directions):
            idx -= len(directions)
        currently = directions[idx]
    # Or add value to the specified direction
    elif action == 'F':
        action = currently
    if action in ('S', 'W'):
        value = -value
    if action in ('N', 'S'):
        ns += value
    elif action in ('E', 'W'):
        ew += value
print(abs(ew) + abs(ns))
