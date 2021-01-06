# Find this puzzle at:
# https://adventofcode.com/2020/day/5

with open('input.txt', 'r') as file:
    puzzle_input = [i for i in file.read().split('\n')]
high_seat_id = 0
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
    high_seat_id = max(high_seat_id, seat_id)
print(high_seat_id)
