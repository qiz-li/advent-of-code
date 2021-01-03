# Put puzzle input into a list
with open('input.txt', 'r') as file:
    puzzle_input = [i.strip('\n') for i in file.readlines()]
occupied = 0
puzzle_input_old = []


def check_seat(y, x, lst):
    """
    Check seat value in a given list.

    Args:
        y: The column index of the seat.
        x: The row index of the seat.
        list: The list the seat is in.

    Returns:
        The value of the seat.
    """
    if y < 0 or x < 0:
        return None
    else:
        try:
            return lst[y][x]
        except IndexError:
            return None


def check_adjacent(y, x, lst):
    """
    Check occupancy of adjacent seats.

    Args:
        y: The column index of the seat.
        x: The row index of the seat.
        list: The list the seat is in.

    Returns:
        The number of occupied seats around the given seat.
    """
    occupied = 0
    col = y - 1
    row = x - 1
    for i in range(9):
        if check_seat(col, row, lst) == "#" and (col, row) != (y, x):
            occupied += 1
        if row - x == 1:
            col += 1
            row -= 3
        row += 1
    return occupied


def run_model(lst):
    """
    Model the seats using the model given: if no adjacent seats are occupied,
    the seat is occupied, if four or more seats are occupied, the seat is
    unoccupied.

    Args:
        list: The list to run the model.

    Returns:
        New list after running the model.
    """
    new_lst = []
    for idx, line in enumerate(lst):
        new_line = ""
        for seat_idx, seat in enumerate(line):
            if seat != ".":
                if check_adjacent(idx, seat_idx, lst) == 0:
                    new_line += ("#")
                elif check_adjacent(idx, seat_idx, lst) >= 4:
                    new_line += ("L")
                else:
                    new_line += lst[idx][seat_idx]
            else:
                new_line += "."
        new_lst.append(new_line)
    return new_lst


# Model list until it no longer changes
while puzzle_input_old != puzzle_input:
    puzzle_input_old = puzzle_input
    puzzle_input = run_model(puzzle_input)
# Find occupied seats!
for line in puzzle_input:
    for seat in line:
        if seat == "#":
            occupied += 1
print(occupied)
