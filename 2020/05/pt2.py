# Find this puzzle at:
# https://adventofcode.com/2020/day/5

with open('input.txt', 'r') as file:
    puzzle_input = file.read().splitlines()
seat_ids = []
for line in puzzle_input:
    col, row = list(range(8)), list(range(128))
    # Slices the existing row or column in half depending on character
    for character in line:
        if character == 'F':
            row = row[:len(row)//2]
        elif character == 'B':
            row = row[len(row)//2:]
        if character == 'L':
            col = col[:len(col)//2]
        elif character == 'R':
            col = col[len(col)//2:]
    seat_id = row[0] * 8 + col[0]
# Find the missing ID in the list of IDs
for idx, seat in enumerate(sorted(seat_ids)):
    if seat + 2 == sorted(seat_ids)[idx + 1]:
        print(seat + 1)
        break
