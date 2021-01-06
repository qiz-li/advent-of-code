# Find this puzzle at:
# https://adventofcode.com/2020/day/11

with open('input.txt', 'r') as file:
    puzzle_input = file.read().splitlines()
occupied = 0
puzzle_input_old = []


def check_directions(y, x, lst):
    """
    Check all directions of a seat for the first seen seats.

    Args:
        y: The column index of the seat.
        x: The row index of the seat.
        list: The list the seat is in.

    Returns:
        The sum of the first visible occupied seats in all
        eight directions of an occupied seat
    """
    occupied = 0
    # The original list input is divided into three parts:
    # rows before the seat, rows after the seat, and the row of the seat.
    # Each direction is then checked, and the value of the first encountered
    # seat is stored in a dictionary. All '#' (occupied seats) in the
    # dictionary are then added up to get the total
    for count, half_lst in enumerate([lst[y+1:], lst[y-1::-1],
                                     [lst[y]] * len(lst[y])]):
        left = right = x
        dct_seats = {0: '.', 1: '.', 2: '.'}
        if y == 0 and count == 1:
            continue
        for row in half_lst:
            if '.' not in dct_seats.values():
                break
            left -= 1
            right += 1
            for idx, item in enumerate([left, x, right]):
                try:
                    if item < 0:
                        continue
                    elif dct_seats.get(idx) == '.':
                        dct_seats[idx] = row[item]
                except IndexError:
                    pass
        occupied += sum(value == '#' for value in dct_seats.values())
    if occupied != 0 and lst[y][x] == '#':
        occupied -= 1
    return occupied


def run_model(lst):
    """
    Model the seats using the model given: if no occupied seats are seen,
    the seat is occupied, if five or more occupied seats are seen, the seat is
    unoccupied.

    Args:
        list: The list to run the model.

    Returns:
        New list after running the model.
    """
    new_lst = []
    # Go through every seat in every line of the input list
    # and make changes to each seat depending on the condition
    for idx, line in enumerate(lst):
        new_line = ''
        for seat_idx, seat in enumerate(line):
            if seat != '.':
                if check_directions(idx, seat_idx, lst) == 0:
                    new_line += ('#')
                elif check_directions(idx, seat_idx, lst) >= 5:
                    new_line += ('L')
                else:
                    new_line += lst[idx][seat_idx]
            else:
                new_line += '.'
        new_lst.append(new_line)
    return new_lst


# Model list until it no longer changes
while puzzle_input_old != puzzle_input:
    puzzle_input_old = puzzle_input
    puzzle_input = run_model(puzzle_input)
# Find occupied seats!
for line in puzzle_input:
    for seat in line:
        if seat == '#':
            occupied += 1
print(occupied)
