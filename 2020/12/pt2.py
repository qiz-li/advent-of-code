# Find this puzzle at:
# https://adventofcode.com/2020/day/12

with open('input.txt', 'r') as file:
    puzzle_input = file.read().splitlines()
ew, ns = 10, 1
sew = sns = 0
for instruc in puzzle_input:
    # Seperate the action and the value
    action = ''.join([i for i in instruc if not i.isdigit()])
    value = int(''.join([i for i in instruc if i.isdigit()]))
    # Ship moves forward to the waypoint by specified number of times
    if action == 'F':
        sns += value * ns
        sew += value * ew
    # If action is to rotate,
    # rotate waypoint around the ship to new coordinates.
    elif action in ('R', 'L'):
        turn = value//90
        if action == 'L':
            turn = 4 - turn
        if turn == 1:
            new_ew = ns
            new_ns = -ew
        elif turn == 2:
            new_ns = -ns
            new_ew = -ew
        elif turn == 3:
            new_ew = -ns
            new_ns = ew
        ew, ns = new_ew, new_ns
    # Or add value to current waypoint coordinates
    if action in ('W', 'S'):
        value = -value
    if action in ('N', 'S'):
        ns += value
    elif action in ('E', 'W'):
        ew += value
print(abs(sew) + abs(sns))
